# Creating the Database

import mysql.connector

database=mysql.connector.connect(host="localhost",user="root",passwd="Password@123")
mycursor=database.cursor()
mycursor.execute("CREATE DATABASE Attendance_Management_System")

