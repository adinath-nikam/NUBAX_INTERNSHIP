
import boto3

import mysql.connector as conn
import psycopg2 as pg
import pandas as pd
from pandas.io import sql
from sqlalchemy import create_engine

import pymysql

from pandas.io import sql

con = conn.connect(host='localhost', database='beneficiary_db', user='root' , passwd='')
query = "SELECT * FROM `beneficiaries` limit 10"
# url = "mysql+pymysql://root:""@127.0.0.1/nb3"
df = sql.read_sql(query, con)
print(df)
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Darsh')




# # response=table.get_item(
# #     Key = {
# #         'emp': '2kl'
# #     }
#
# # )
# # print(response['Item'])
#
#