# Data Migration from Postgresql to MySQL

# 1. Sync psql table to mysql

# Read data from psql table and write it to mysql using pandas dataframe
# Source readonly


import psycopg2 as pg
import pandas as pd
from sqlalchemy import create_engine

import pymysql

from pandas.io import sql


engine = pg.connect("dbname='' user='' host='' port='' password=''")
df = pd.read_sql('select * from beneficiaries', con=engine)


print(df);

url = "mysql+pymysql://root:""@127.0.0.1/beneficiary_db"

#engine = create_engine("mysql+pymysql://" + "root" + ":" + "" + "@" + "127.0.0.1" + "/" + "db_name_here")

engine = create_engine(url)
df.to_sql('df', con = engine, if_exists = 'replace')

print("Done")
