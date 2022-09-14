import pyarrow as pa
import redis
import mysql.connector as connection
from  pandas.io import sql
from csv import reader

# host - Host, port - Port No., db - Database Number

redisConnectionPool = redis.ConnectionPool(host='localhost', port=6379, db=0)
redisConn = redis.Redis(connection_pool=redisConnectionPool)
sqlConn = connection.connect(host="localhost", database = "redistemp", user="root", passwd="")

# Set Value
# redisConn.set('this_is_key', 'this is key value')

# Get Value
# print(redisConn.get('this_is_key'))


query = "Select * from redistbl"
df = sql.read_sql(query, sqlConn)

def MySQLtoRedis(keyValue, dataframe):
    df = pa.serialize(dataframe).to_buffer().to_pybytes()
    result = redisConn.set(keyValue,df)
    if result == True:
        print('Upload Done')

def LoadfromRedis(keyValue):
    data = redisConn.get(keyValue)
    try:
        return pa.deserialize(data)
    except:
        print("No data")


MySQLtoRedis('this_is_key', df)

LoadfromRedis('this_is_key')
