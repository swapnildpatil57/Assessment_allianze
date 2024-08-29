import pyodbc


server="DESKTOP-Q0CENEN\SQLEXPRESS"
database ="sample1"
username="sampleusr"
password="sampleusr1"


connect_str=f'DRIVER={{SQL Server}};server={server};database={database};user={username};password={password}'


connect=pyodbc.connect(connect_str)

row=connect.cursor()

result=row.execute("select * from employees")

result=row.fetchall()

for i in result:
    print (i[1]+" patil")

