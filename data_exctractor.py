import mysql.connector
import pandas as pd


tables=['customers','date','markets','products','transactions']

cnx = mysql.connector.connect(user='root', password='srinidhi', host='localhost', port=3306, database='sales')


for table_name in tables:
    query=f"Select * from {table_name}"
    df=pd.read_sql_query(query,cnx)
    df.to_csv(f"datasets/{table_name}.csv")