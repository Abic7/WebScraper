import os
import argparse

from time import time

import pandas as pd
from sqlalchemy import create_engine

def main(params):

    # Declare the ingestion script parameters
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    table_name = params.table_name
    url = params.url
    csv_name = 'output.csv'

    # Download CSV file from URL
    os.system(f"wget {url} -O {csv_name}")

    # Connect to Postgres with SQLAlchemy
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    
    # Convert datetime fields to pandas datetime objects
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    # Convert schema to DDL with SQLAlchemy
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
    
     # Insert data into Postgres database by chunks
    df_iter = pd.read_csv(csv_name, iterator=True, chunksize=100000)
    df = next(df_iter)

    # Insert data frame values in Postgres database
    df.to_sql(name=table_name, con=engine, if_exists='append')

    # Time the ingestion process and print status
    while True: 
        t_start = time()

        df = next(df_iter)

        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        df.to_sql(name=table_name, con=engine, if_exists='append')

        t_end = time()

        print('inserted another chunk, took %.3f second' % (t_end - t_start))