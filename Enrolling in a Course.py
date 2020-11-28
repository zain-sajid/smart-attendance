#Enrolment of Students

import mysql.connector

def add_student(course_name,student_name,cms_id):
    database=mysql.connector.connect(host="localhost",user="root",passwd="",database="attendance_management_system")
    mycursor=database.cursor()

    cms_id=int(cms_id)
    
    mycursor.execute(f"INSERT INTO {course_name} (Name,CMS_ID) VALUES('{student_name}',{cms_id})")
    
    database.commit()

course_name = input("Enter the course code: ")
student_name = input("Enter the name: ")
cms_id = input("Enter the CMS ID: ")

add_student(course_name,student_name,cms_id)

