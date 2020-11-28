#Appending Absent For Scanned Codes

import mysql.connector

def append_absent(table_name,attendance_date):
    database=mysql.connector.connect(host="localhost",user="root",passwd="Password@123",database="Attendance_Management_System")

    mycursor=database.cursor()
    print(attendance_date)
    mycursor.execute(f"UPDATE {table_name} SET {attendance_date}='Absent' WHERE {attendance_date}=''")
    database.commit()

