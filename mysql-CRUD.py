# ----------- establish connection, insert data into the table

import MySQLdb as sql

host='localhost'
user='root'
password='root12345'
port=3306
db='crud'
query= "INSERT INTO user_table VALUES (2, 'fuji', '25')"
# query= "INSERT INTO user_table (id, age) VALUES (2, '25')"

conn=sql.Connection(host=host, user=user, password=password, port=port, db=db)
cursor=conn.cursor()
result=cursor.execute(query)
conn.commit()
conn.close()
if result==1:
    print("Data inserted successfully") 
else:
    print("Error") 


# ----------- establish connection, insert data during runtime

import MySQLdb as sql

host='localhost'
user='root'
password='root12345'
port=3306
db='crud'

# Get input from user
id=int(input("Please enter Id"))
name=str(input("Please enter name"))
age=int(input("Please enter age"))

# create tuple using the given data
data = (id, name, age)      

# create query
query= "INSERT INTO user_table VALUES (%s, %s, %s)"
# query= "INSERT INTO user_table (id, name, age) VALUES (%s, %s, %s)"

conn=sql.Connection(host=host, user=user, password=password, port=port, db=db)
cursor=conn.cursor()

# send query and data to execute
result=cursor.execute(query, data)

conn.commit()
conn.close()
if result==1:
    print("Data inserted successfully")    
else:
    print("Error")    


# ----------- establish connection, insert data during runtime

# Get data check the id in table, if already exist give error 
# message else save data in the table

import MySQLdb as sql

host='localhost'
user='root'
password='root12345'
port=3306
db='crud'

# Get input from user
id=int(input("Please enter Id "))
name=str(input("Please enter name "))
age=int(input("Please enter age "))

# create tuple using the given input
data = (id, name, age)      

# create search query
getQuery= "SELECT * FROM crud.user_table WHERE id=%s"

# create query
insertQuery= "INSERT INTO user_table VALUES (%s, %s, %s)"

# query= "INSERT INTO user_table (id, name, age) VALUES (%s, %s, %s)"

conn=sql.Connection(host=host, user=user, password=password, port=port, db=db)
cursor=conn.cursor()

# execute query to find given id is already in table
cursor.execute(getQuery,(id,))      

# if found retreive all and store in result_getQuery
result_getQuery=cursor.fetchall()
print(result_getQuery)

# if result_getQuery is true, data already in table else insert data in table
if (result_getQuery):
    print("User Id already exist, insertion failed")
else:
    print("User Id does not exist")

    # send query and data to execute
    # if successfully inserted the cursor will return 1 to the result
    result=cursor.execute(insertQuery, data)
    
    conn.commit()
    conn.close()

    # check if the data is inserted in table by 
    if result==1:
        print("Data inserted successfully")    
    else:
        print("Error")    


# ----------- establish connection, insert multiple records 

import MySQLdb as sql

host='localhost'
user='root'
password='root12345'
port=3306
db='crud'

# store data that to be inserted in a list with tuple
data = [(1, 'ibm', 35),(2, 'intel', 40),(3, 'microsoft', 30),(4, 'apple', 29),]      

# create query
insertQuery= "INSERT INTO user_table VALUES (%s, %s, %s)"

# insertQuery= "INSERT INTO user_table (id, name, age) VALUES (%s, %s, %s)"

conn=sql.Connection(host=host, user=user, password=password, port=port, db=db)
cursor=conn.cursor()

# send query and data to execute many items repeatedly
# if successfully inserted, the cursor will return total record inserted
result=cursor.executemany(insertQuery, data)

conn.commit()
conn.close()

# check is all data inserted in table
if result==len(data):
    print("Data inserted successfully")    
else:
    print("Error")   


# ----------- establish connection, simple update records 

import MySQLdb as sql

host='localhost'
user='root'
password='root12345'
port=3306
db='crud'
conn=sql.Connection(host=host, user=user, password=password, port=port, db=db)

# create query
updateQuery= "UPDATE user_table SET name='Google' WHERE id=1"           # one field
# updateQuery= "UPDATE user_table SET name='Google', age=20 WHERE id=1"     # multiple field

cursor=conn.cursor()

# send query to update
# if successfully updatted, the cursor will return total record updatted
result=cursor.execute(updateQuery)

conn.commit()
conn.close()

# check is all data updated in table
if result==1:
    print("Data updated successfully")    
else:
    print("Error")    


# ----------- establish connection, update records on runtime 

import MySQLdb as sql

host='localhost'
user='root'
password='root12345'
port=3306
db='crud'
conn=sql.Connection(host=host, user=user, password=password, port=port, db=db)

id=3
name='TCS'

# store data that to be updated in a list with tuple
# place the variable as per query values(first %s is name and second %s is id)
data = (name,id)

# create search query
getQuery= "SELECT * FROM crud.user_table WHERE id=%s"
# create query
updateQuery= "UPDATE user_table SET name=%s WHERE id=%s"   # one field

cursor=conn.cursor()

# execute query to find given id is already in table
cursor.execute(getQuery,(id,))      

# if found retreive all and store in result_getQuery
result_getQuery=cursor.fetchall()
print(result_getQuery)

# if result_getQuery is true, record exist update the table else error message
if (result_getQuery):
    result=cursor.execute(updateQuery, data)
    conn.commit()
    conn.close()

    # check is all data updated in table
    if result==1:
        print("Data updated successfully")    
    else:
        print("Error")
else:
    print("User Id does not exist")


# ----------- establish connection, delete record on runtime 

import MySQLdb as sql

host='localhost'
user='root'
password='root12345'
port=3306
db='crud'
conn=sql.Connection(host=host, user=user, password=password, port=port, db=db)

id=3

# create search query
getQuery= "SELECT * FROM crud.user_table WHERE id=%s"
# create query
deleteQuery= "DELETE FROM user_table WHERE id=%s"   # one field

cursor=conn.cursor()

# execute query to find given id is already in table
cursor.execute(getQuery,(id,))      

# if found retreive all and store in result_getQuery
result_getQuery=cursor.fetchall()
print(result_getQuery)

# if result_getQuery is true, record exist delete from table else error message
if (result_getQuery):
    result=cursor.execute(deleteQuery, (id,))
    conn.commit()
    conn.close()

    # check is data deleted from table
    if result==1:
        print("Record deleted successfully")    
    else:
        print("Error")
else:
    print("User Id does not exist")


# ----------- establish connection, delete record on runtime 

import MySQLdb as sql

host='localhost'
user='root'
password='root12345'
port=3306
db='crud'
conn=sql.Connection(host=host, user=user, password=password, port=port, db=db)

id = (3)

def findRecord(id):

    print("in for statement ", id)

    # create search query
    getQuery= "SELECT * FROM crud.user_table WHERE id=%s"

    cursor=conn.cursor()

    # store the record to be deleted in 
    # execute query to find given id is already in table
    cursor.execute(getQuery,(id,))      

    # if found retreive all and store in result_getQuery
    result_getQuery=cursor.fetchall()
    print(result_getQuery)

    # if result_getQuery is true, record exist delete from table else error message
    if (result_getQuery):
        recordDelete(id)
    else:
        print("User Id does not exist")

def recordDelete(record):
    # print("Record found ",record)
    record=record
    # # create query
    deleteQuery= "DELETE FROM user_table WHERE id=%s"   # one field
    cursor=conn.cursor()
    result=cursor.execute(deleteQuery, (record,))
    print(result)
    conn.commit()
    conn.close()

    # check is data deleted from table
    if result==1:
        print("Record deleted successfully")    
    else:
        print("Error")

findRecord(id)
