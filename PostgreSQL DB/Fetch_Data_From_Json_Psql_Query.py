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




jso = pd.DataFrame({"beneficiaries": [ {"db_name": "beneficiary_db", "data_mart_table": "ration_appointments_validation",
  "psql_query": "select * from ration_appointments_validation as sd where true"
                                        },
 {"db_name": "beneficiary_db", "data_mart_table": "beneficiary_address",
"psql_query": "select sd.*, b.project_id from beneficiary_address sd JOIN beneficiaries b on "
 "sd.beneficiary_id=b.id "},
{"db_name": "beneficiary_db", "data_mart_table": "beneficiary_ration_details",
 "psql_query": "select sd.*, b.project_id from beneficiary_ration_details sd JOIN beneficiaries b on "
 "sd.beneficiary_id=b.id "},
 {"db_name": "beneficiary_db", "data_mart_table": "ration_appointments",
 "psql_query": "select * from ration_appointments as sd where true"}
 ]})



# print(df)


for column_name, item in jso.iteritems():

    for i in range(len(item)):
        df=(item[i]["psql_query"])
        print(df)

engine = pg.connect("dbname='beneficiary_db' user='dbreaduser' host='3.7.81.85' port='5432' password='DBPROD@read$#$'")

query = pd.read_sql_query(df, con=engine)


url = "mysql+pymysql://root:""@127.0.0.1/nb3"
# engine = create_engine("mysql+pymysql://" + "root" + ":" + "" + "@" + "127.0.0.1" + "/" + "beneficiary_db")
engine = create_engine(url)



query.to_sql('psql', con = engine, if_exists = 'replace')
print("Done")
