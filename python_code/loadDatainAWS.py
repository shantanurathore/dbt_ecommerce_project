import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import Index

# SQLAlchemy setup
Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'

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
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    # Upload data in chunks
    chunk_size = 1000
    for i in range(0, len(df), chunk_size):
        chunk = df.iloc[i:i+chunk_size]
        records = chunk.to_dict('records')
        session.bulk_insert_mappings(Transaction, records)
        session.commit()
        print(f"Uploaded records {i+1} to {i+len(chunk)}")

    session.close()

if __name__ == "__main__":
    # Generate the data
    df = generate_ecommerce_data(100000)

    # AWS MySQL connection string
    # Replace with your actual AWS MySQL connection details
    db_url = "mysql+pymysql://username:password@your-aws-mysql-endpoint:3306/your_database_name"

    # Upload to AWS
    upload_to_aws(df, db_url)

    print("Data generated and uploaded to AWS MySQL")
    print(df.head())
    print(f"\nDataset shape: {df.shape}")