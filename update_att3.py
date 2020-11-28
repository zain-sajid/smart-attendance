#Updating Attendance of Students

import mysql.connector
import tkinter

def update_attendance(table_name,attendance_date,name,cms_id):
        try:
                database=mysql.connector.connect(host="localhost",user="root",passwd="Password@123",database="Attendance_Management_System")

                mycursor=database.cursor()

                sqlFormula=f"UPDATE {table_name} SET {attendance_date}='Present' WHERE Name='{name}' AND CMS_ID={cms_id}"
                mycursor.execute(sqlFormula)
                tkinter.messagebox.showinfo('Attendance Marked', 'Your Attendance has been marked successfully in {} course'.format(table_name))
                database.commit()
        except:
                tkinter.messagebox.showerror('ERROR','You are not enrolled in this course')

