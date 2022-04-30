# Data Migration from Postgresql to MySQL
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
