#Creating Tables For Courses in Database

import mysql.connector

def create_table_for_course(course_name):
    database=mysql.connector.connect(host="localhost",user="root",passwd="Password@123",database="Attendance_Management_System")
    mycursor=database.cursor()
    mycursor.execute(f"CREATE TABLE IF NOT EXISTS {course_name} (Name VARCHAR(30) NOT NULL,CMS_ID INTEGER(6) NOT NULL)")
    
course_name=input("Enter Course Name: ")
create_table_for_course(course_name)
