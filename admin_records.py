#Retrievel of Records from the Database

import mysql.connector

def course_records(table_name):
    database=mysql.connector.connect(host="localhost",user="root",passwd="Password@123",database="Attendance_Management_System")
    mycursor=database.cursor()
    
    mycursor.execute(f"SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME='{table_name}' ORDER BY ORDINAL_POSITION")
    column_titles=mycursor.fetchall()
    print(column_titles)

    mycursor.execute(f"SELECT * FROM {table_name} ORDER BY Name")
    records=mycursor.fetchall()
    print(records)

course_records('phy102')