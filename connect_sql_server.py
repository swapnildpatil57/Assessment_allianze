import pyodbc

# Parameters for connecting to your SQL Server
server = 'DESKTOP-Q0CENEN\SQLEXPRESS'  # Replace with your server name
database = 'sample1'  # Replace with your database name
username = 'sampleusr1'  # Replace with your username
password = '1234'  # Replace with your password

# Create a connection string
conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Connect to the database
try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    # Example query
    cursor.execute('select * from employee;')

    # Fetch and print the first row
    rows = cursor.fetchall()
    for i in rows:
        print (i)
    #print('SQL Server version:', row[0])

    # Optionally, you can fetch all results
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)

    # Close connections
    cursor.close()
    conn.close()

except pyodbc.Error as e:
    print(f'Error connecting to SQL Server: {e}')
