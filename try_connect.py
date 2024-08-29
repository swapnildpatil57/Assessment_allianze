

import csv
import pyodbc


import pandas as pd

#pd.options.display.max_rows = 9999


server = 'DESKTOP-Q0CENEN\SQLEXPRESS'  # Replace with your server name
database = 'sample1'  # Replace with your database name
username = 'sampleusr1'  # Replace with your username
password = '1234'  # Replace with your password




conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()


path='C:\\Users\\swapnil patil\\Desktop\\Book1.csv'

df = pd.read_csv(path)

print(df)


with open (path , 'r') as file:
    reader=csv.reader(file)
    next(reader)

    for row in reader:
        row[0]=row[0]+ '1'
        row[1]=row[1]+ 'a'
        #cursor.execute('select * from employee')
        cursor.execute('insert into employee (employee_id, name) values (?,?);', (row[0],row[1]))


conn.commit()
conn.close()

print("Data inserted successfully into SQLserver table.")

