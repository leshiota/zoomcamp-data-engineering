import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse
import os

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    parquet_name ='output.parquet'
   

    os.system(f'wget {url} -O {parquet_name}')

    df = pd.read_parquet('output.parquet', engine='pyarrow')
    print(df)


    engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)



    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')
    df.to_sql(name=table_name, con=engine, if_exists='append')


if __name__== '__main__':

    parser = argparse.ArgumentParser(description='Ingest cvs data to Postegres')

    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='table name for postgres')
    parser.add_argument('--url', help='url of cvs file')

    args = parser.parse_args()

    main(args)