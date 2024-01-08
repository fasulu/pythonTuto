# ----------- establish connection, show table list and create new table

import MySQLdb as sql

host='localhost'
user='root'
password='root12345'
port=3306
db='crud'

conn=sql.Connection(host=host, user=user, password=password, port=port, db=db)
cursor=conn.cursor()
show='show tables'
cursor.execute(show)
result=cursor.fetchall()
print(result)               # prints the all table names
for x in result:
    print(x)                # iterates tables one by one

createTable_Query= "CREATE TABLE `user_table` (`id` int NOT NULL,`name` varchar(45) DEFAULT NULL,`age` varchar(45) DEFAULT NULL,PRIMARY KEY (`id`))"
cursor.execute(createTable_Query)
cursor.execute(show)
result=cursor.fetchall()
print(result)               # prints the all table names
