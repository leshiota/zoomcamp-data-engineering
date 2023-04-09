import sys

import pandas as pd

print(sys.argv)

day = sys.argv[1]

print(f'job finished sucessufly for day = {day}')

URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"

python ingest_data.py \
  --user=root \
  --password=root \
  --host=pg-database2 \
  --port=5432 \
  --db=ny_taxi \
  --table_name=yellow_taxi_trips_records \
  --url='https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet'