import mysql.connector
import pandas as pd
mydb = mysql.connector.connect(user='root', password='srinidhi', host='localhost', port=3306, database='sales')
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM markets")
myresult = mycursor.fetchall()
markets_data = pd.DataFrame(myresult)
print(markets_data.shape
