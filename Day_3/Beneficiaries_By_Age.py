#No of beneficiaries by the age group and the gender;
from logging import exception
import pandas as pd
import psycopg2 as pg
from sqlalchemy import *
import pymysql
import mysql.connector as connection

try:
    conn = connection.connect(host="localhost", database = "beneficiary_db", user="root", passwd="")
    query = 'select count(id),age,gender from beneficiary_family group by age, gender'
    df = pd.read_sql(query, conn)
    print(df)

except exception as e:
    print(str(e))
    conn.close()