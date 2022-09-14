# Imports of Libraries
import psycopg2 as pg
import pandas as pd
from sqlalchemy import create_engine
import pymysql
from pandas.io import sql

# 1. Migrate The Data from Postgrsql to Local MySQL Server in CHUNKS

# Establish Connection With Postgresql Server
engine = pg.connect("dbname='beneficiary_db' user='dbreaduser' host='3.7.81.85' port='5432' password='DBPROD@read$#$'")

 # Get The Data In Chunks of Size 100
df = pd.read_sql_query('select * from beneficiary_address', con=engine, chunksize=100)


# Push the DATA IN CHUNKS
for data in df:
    
    # print(data)

    # Establish Connection With Local Mysql Server
    url = "mysql+pymysql://root:""@127.0.0.1/beneficiary_db"

    engine = create_engine(url)
    
    # Store The Data In Local MySQL
    data.to_sql('beneficiary_address', con = engine, if_exists = 'replace')


print("Done.")
