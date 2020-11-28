#Resetting Mac Addresses after every Lecture

import mysql.connector

def reset_mac():
    database=mysql.connector.connect(host="localhost",user="root",passwd="Password@123",database="Attendance_Management_System")
    mycursor=database.cursor()
    mycursor.execute("UPDATE Mac_Address SET Mac_Addresses=''")
    database.commit()

#reset_mac()

    



