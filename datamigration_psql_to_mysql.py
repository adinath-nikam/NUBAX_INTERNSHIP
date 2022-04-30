# Data Migration from Postgresql to MySQL

# 1. Sync psql table to mysql

# Read data from psql table and write it to mysql using pandas dataframe
# Source readonly
# Table : beneficiaries
# DB : beneficiary_db
# psql_server = "3.7.81.85"
# psql_username = "dbreaduser"
# psql_password = "DBPROD@read$#$"
# Destination : setup mysql on localhost and write in beneficiary_db (create new db on localhost through code)


import psycopg2 as pg
import pandas as pd
from sqlalchemy import create_engine

import pymysql

from pandas.io import sql


engine = pg.connect("dbname='beneficiary_db' user='dbreaduser' host='3.7.81.85' port='5432' password='DBPROD@read$#$'")
df = pd.read_sql('select * from beneficiaries', con=engine)


print(df);

url = "mysql+pymysql://root:""@127.0.0.1/beneficiary_db"

#engine = create_engine("mysql+pymysql://" + "root" + ":" + "" + "@" + "127.0.0.1" + "/" + "beneficiary_db")

engine = create_engine(url)
df.to_sql('df', con = engine, if_exists = 'replace')

print("Done")
