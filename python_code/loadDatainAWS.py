import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import Index
from dotenv import load_dotenv
import os


# SQLAlchemy setup
Base = declarative_base()

# Load environment variables from .env file
load_dotenv()

# Retrieve sensitive data from environment variables
DATABASE_URL = os.getenv('DATABASE_URL')

class Transaction(Base):
    """
    SQLAlchemy ORM class for the ecomm_transactions table.
    
    Attributes:
        transaction_id (int): Primary key for the transaction.
        user_id (int): ID of the user making the transaction.
        product_id (int): ID of the product being purchased.
        timestamp (datetime): Timestamp of the transaction.
        purchase_amount (float): Amount of the purchase.
        product_category (str): Category of the product.
        user_location (str): Location of the user.
    """
    __tablename__ = 'ecomm_transactions'

    transaction_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True)
    product_id = Column(Integer, index=True)
    timestamp = Column(DateTime, index=True)
    purchase_amount = Column(Float)
    product_category = Column(String(50))
    user_location = Column(String(2))

    # Create additional indexes
    __table_args__ = (
        Index('ix_category_location', 'product_category', 'user_location'),
        Index('ix_amount', 'purchase_amount'),
    )

def generate_ecommerce_data(num_records=100000):
    """
    Generates a DataFrame with synthetic e-commerce transaction data.
    
    Args:
        num_records (int): Number of records to generate. Default is 100,000.
    
    Returns:
        pd.DataFrame: DataFrame containing the generated data.
    """
    np.random.seed(42)
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    dates = pd.date_range(start=start_date, end=end_date, periods=num_records)

    data = {
        'transaction_id': range(1, num_records + 1),
        'user_id': np.random.randint(1, 10001, num_records),
        'product_id': np.random.randint(1, 1001, num_records),
        'timestamp': dates,
        'purchase_amount': np.round(np.random.uniform(1, 100, num_records), 2),
        'product_category': np.random.choice(['Game', 'App', 'In-app Purchase'], num_records),
        'user_location': np.random.choice(['US', 'UK', 'CA', 'AU', 'DE', 'FR', 'JP'], num_records)
    }

    return pd.DataFrame(data)

def upload_to_aws(df, db_url):
    """
    Uploads the DataFrame to an AWS database.
    
    Args:
        df (pd.DataFrame): DataFrame containing the data to upload.
        db_url (str): Database URL for the AWS database.
    
    Returns:
        None
    """
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    # Upload data in chunks
    chunk_size = 1000
    for i in range(0, len(df), chunk_size):
        chunk = df.iloc[i:i+chunk_size]
        records = chunk.to_dict('records')
        # Add records to the session and commit
        session.bulk_insert_mappings(Transaction, records)
        session.commit()

    session.close()

if __name__ == "__main__":
    # Generate the data
    df = generate_ecommerce_data(100000)

    # AWS MySQL connection string
    # Replace with your actual AWS MySQL connection details
    db_url = "mysql+pymysql://admin:passwordpatanahi@dsprojectsdb1.c34e2eieueaa.us-east-2.rds.amazonaws.com/ecomm_transactions_db"

    # Upload to AWS
    upload_to_aws(df, db_url)

    print("Data generated and uploaded to AWS MySQL")
    print(df.head())
    print(f"\nDataset shape: {df.shape}")
