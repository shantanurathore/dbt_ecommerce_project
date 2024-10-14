# E-commerce Data Analysis Project

## Project Overview
This project involves generating synthetic e-commerce data, storing it in an AWS MySQL database, and setting up a data analysis environment using dbt (data build tool). The project also includes Git version control for managing the codebase.
This can serve as an example project for someone trying to learn dbt and implement it locally.
This setup was done on a mac. The process will have significant changes 

## Components

### 1. Synthetic E-commerce Data Generator
- Python script to generate realistic e-commerce transaction data
- Uses pandas and numpy for data generation
- Includes user IDs, product IDs, timestamps, purchase amounts, product categories, and user locations
- Capable of generating large datasets (default: 100,000 records)

### 2. Database Integration
- Utilizes SQLAlchemy to define a `Transaction` model
- Implements indexing for better query performance
- Uploads generated data to an AWS MySQL database

### 3. dbt Configuration
- Set up for MySQL integration
- Configured to connect to the AWS RDS MySQL instance

### 4. Version Control
- Git repository initialized for the project
- Guide included for Git setup and basic usage

## Setup and Usage

### Prerequisites
- Python 3.x
- Git
- Access to an AWS RDS MySQL instance

### Configuration
1. Update the AWS MySQL connection string in the data generator script
2. Configure the dbt profile in `~/.dbt/profiles.yml` using the provided template

### Running the Data Generator
```
python synthetic_ecommerce_data_generator.py
```

### Using dbt
- Initialize your dbt project
- Create models for data transformation
- Run dbt commands to build your data warehouse

## File Structure
- `synthetic_ecommerce_data_generator.py`: Main script for data generation and upload
- `profiles_eg.yml`: dbt profile configuration
- `README.md`: This file
- Additional dbt and analysis files (to be added)

## Git Workflow
Refer to the included Git Setup and Usage Guide (gitHelpDoc.md) for detailed instructions on:
- Setting up Git
- Pushing new code
- Creating branches
- Merging changes


## Next Steps
- Develop dbt models for data transformation
- Create data visualizations and dashboards
- Implement automated testing for data quality
- Set up CI/CD pipeline for the project