import os
import pyodbc
import env


# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

#server = 'tcp:blaireau.database.windows.net,1433'
server=os.getenv('SQL_SERVER')
database=os.getenv('SQL_DATABASE')
username=os.getenv('SQL_USER')
password=os.getenv('SQL_PASSWORD')

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute("SELECT TOP(10) * FROM LoveRunningQueries")

for row in cursor.fetchall():
    print(row)