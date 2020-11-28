#Updating Attendance of Students

import mysql.connector
import tkinter.messagebox

def update_attendance(table_name,attendance_date,name,cms_id):
    database=mysql.connector.connect(host="localhost",user="root",passwd="Password@123",database="Attendance_Management_System")

    mycursor=database.cursor()
    mycursor.execute(f"SELECT Name,CMS_ID FROM {table_name}")
    authentic_credentials=mycursor.fetchall()
    print(type(authentic_credentials))
    #check_student="('{}', {})".format(name,cms_id)
    cms_id = int(cms_id)
    check_student=(f'{name}',cms_id)
    print(check_student)
    for i in range(len(authentic_credentials)):
        if(authentic_credentials[i]==check_student):
            database=mysql.connector.connect(host="localhost",user="root",passwd="Password@123",database="Attendance_Management_System")
            mycursor2=database.cursor()
            sqlFormula=f"UPDATE {table_name} SET {attendance_date}='Present' WHERE Name='{name}' AND CMS_ID={cms_id}"
            mycursor2.execute(sqlFormula)
            tkinter.messagebox.showinfo('Attendance Marked', 'Your Attendance has been marked successfully in {} course'.format(table_name))
            database.commit()
            check = 1
            print("You are Clear to GO!")
            break
    else:
        tkinter.messagebox.showerror('ERROR','You are not enrolled in this course')
        check = 0
        print("Invalid Name or CMS ID")

#update_attendance('phy102','22_12_2019_Lec1','phyguy','222222')
