import pandas as pd
import psycopg2 as pg
from sqlalchemy import *
import pymysql
import mysql.connector as connection
from pandas.io import sql


try:
    conn = connection.connect(host="localhost", database = "beneficiary_db", user="root", passwd="", )

    query = 'select count(state),state from beneficiary_address group by state'
    df = pd.read_sql(query, conn)
    print(df)

except Exception as e:
    print(str(e))