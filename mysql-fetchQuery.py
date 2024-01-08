# ----------- establish connection, send query, store fetched result and print result

import MySQLdb as sql

host='localhost'
user='root'
password='root12345'
port=3306
db='crud'

conn=sql.Connection(host=host, user=user, password=password, port=port, db=db)
cursor=conn.cursor()
cursor.execute("""SELECT * FROM crud.products""")
print(cursor.rowcount)      # gives total rows fetched from the table
# result=cursor.fetchall()  # stores all rows from the table
# result=cursor.fetchone()  # stores first row
# result=cursor.fetchmany() # stores all rows
result=cursor.fetchmany(5)  # stores first 5 rows
print(result)               # prints the stored result