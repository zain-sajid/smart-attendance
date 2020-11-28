#Manually overriding Attendance Records

import mysql.connector
import tkinter.messagebox

def manual_override(table_name,attendance_date,attendance_status,cms_id):

    database=mysql.connector.connect(host="localhost",user="root",passwd="Password@123",database="Attendance_Management_System")

    mycursor=database.cursor()

    sqlFormula=f"UPDATE {table_name} SET {attendance_date}='{attendance_status}' WHERE CMS_ID={cms_id}"
    mycursor.execute(sqlFormula)
    database.commit()
    tkinter.messagebox.showinfo('Attendance Marked', '{} has been marked {} successfully in {} course'.format(cms_id,attendance_status,table_name))
