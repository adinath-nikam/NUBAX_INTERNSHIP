# Day 2, Assignment - 2
# lets get some stats on beneficiary  table using pandas dataframe like
# 1.total number of beneficiaries
# 2.total number by gender
# 3.what max and min age
# 5.group by qualification 

import mysql.connector as connection
import pandas as pd
from pandas.io import sql

try:

    conn = connection.connect(host="localhost", database = 'beneficiary_db', user="root", passwd="",use_pure=True)
    query = "Select * from df"
    df = sql.read_sql(query, conn)
    
    # print(df)

    # 1. Total Beneficiaries
    # print(len(df.index))
    # print(df[df.columns[0]].count())

    # 2. Total Number by Gender
    # print(df.groupby('gender').size())

    # 3. what max and min age
    # print(df['age'].max())

    # 4. Group by Qualification 
    # print(df.groupby('highest_educational_qualification').count())

    conn.close() #close the connection
    
except Exception as e:
    conn.close()
    print(str(e))
