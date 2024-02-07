import sqlite3

#Connect to sqllite
connection=sqlite3.connect("student.db")

#create a cursor for insertion of records,table creation

cursor=connection.cursor()

#table creation
table_info="""
create table STUDENT(NAME varchar(25),CLASS VARCHAR(25),
SECTION varchar(25),MARKS int);
"""
cursor.execute(table_info)

#Record Insertion

cursor.execute('''Insert into STUDENT values('Tarun','CS','C',150)''')
cursor.execute('''Insert into STUDENT values('Sarthak','CS','C',150)''')
cursor.execute('''Insert into STUDENT values('Akshat','EN','A',100)''')
cursor.execute('''Insert into STUDENT values('Karan','ECE','B',90)''')
cursor.execute('''Insert into STUDENT values('Varun','CSE','B',100)''')

#Display the records

print("The Inserted records are:")

data=cursor.execute('''select * from STUDENT''')

for row in data:
    print(row)

#Commit and close the connection

connection.commit()
connection.close()