#Creating Columns For Attendance

import mysql.connector
import tkinter.messagebox

def attendance_column(course_name,attendance_date):
    database=mysql.connector.connect(host="localhost",user="root",passwd="Password@123",database="Attendance_Management_System")

    mycursor=database.cursor()

    try:
        mycursor.execute(f"ALTER TABLE {course_name} ADD COLUMN ({attendance_date+'_Lec1'} VARCHAR(10) DEFAULT '' NOT NULL)")
        lecture_count = attendance_date+'_Lec1'
        
    except:
        try:
            mycursor.execute(f"ALTER TABLE {course_name} ADD COLUMN ({attendance_date+'_Lec2'} VARCHAR(10) DEFAULT '' NOT NULL)")
            lecture_count = attendance_date+'_Lec2'
        except:
            try:
                mycursor.execute(f"ALTER TABLE {course_name} ADD COLUMN ({attendance_date+'_Lec3'} VARCHAR(10) DEFAULT '' NOT NULL)")
                lecture_count = attendance_date+'_Lec3'
            except:
                try:
                    mycursor.execute(f"ALTER TABLE {course_name} ADD COLUMN ({attendance_date+'_Lec4'} VARCHAR(10) DEFAULT '' NOT NULL)")
                    lecture_count = attendance_date+'_Lec4'
                except:
                    tkinter.messagebox.askquestion('MISSION : TERMINATE All STUDENTS','Do you want to continue with your mission?')

    return lecture_count
#course_name=input("Enter Course Name: ")
#attendance_date=input("Enter Date for Attendance: ")

#attendance_column('hu100','19_12_2019')
