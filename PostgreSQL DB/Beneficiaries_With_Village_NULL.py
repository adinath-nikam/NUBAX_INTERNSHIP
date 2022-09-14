import pandas as pd
import psycopg2 as pg
from sqlalchemy import *
import pymysql
import mysql.connector as connection
from pandas.io import sql

try:
    conn = connection.connect(host="localhost", database="beneficiary_db", user="root", passwd="", )

    query = 'select count(ISNULL(village)) as "Count of NULL Villages" from beneficiary_address WHERE village IS NULL'
    df = pd.read_sql(query, conn)
    print(df)


except Exception as e:
    print(str(e))