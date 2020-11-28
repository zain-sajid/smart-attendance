#Enrollment of Students

import mysql.connector
import tkinter.messagebox

def add_student(course_name,student_name,cms_id):
    #to_be_or_not_to_be = 0
    course = course_name
    if course=='Fundamentals of Programming':
        course = 'cs114'
    elif course=='Discrete Mathematics':
        course = 'math161'
    elif course=='Calculus and Analytic Geometry':
        course = 'math101'
    elif course=='Islamic Studies':
        course = 'hu101'
    elif course=='English':
        course = 'hu100'
    elif course=='Applied Physics':
        course = 'phy102'

    print(student_name)
    if len(cms_id)==6 and student_name!='':
        database=mysql.connector.connect(host="localhost",user="root",passwd="Password@123",database="Attendance_Management_System")
        mycursor=database.cursor()
        print('yes it doth')
        mycursor.execute(f"SELECT CMS_ID FROM {course}")
        authentic_credentials=mycursor.fetchall()
        try:
            cms_id=int(cms_id)
            check_student=(cms_id,)
            print(check_student)
            print(type(check_student))
            for i in range(len(authentic_credentials)):
                #print(authentic_credentials)
                if(authentic_credentials[i]==check_student):
                    print("Student already exists")
                    #to_be_or_not_to_be = 1
                    message1 = student_name+' is already enrolled in '+course
                    tkinter.messagebox.showinfo('ALREADY ENROLLED',message1)
                    break
            else:
                print('it runs nigga')
                mycursor.execute(f"INSERT INTO {course} SET Name='{student_name}',CMS_ID={cms_id}")
                mycursor.execute(f"INSERT INTO Mac_Address SET Name='{student_name}',CMS_ID={cms_id}")
                message = student_name+' has been enrolled '+course
                tkinter.messagebox.showinfo('ENROLLED', message)
                database.commit()
        except:
            tkinter.messagebox.showerror('INVALID CMS ID', 'CMS ID is invalid')

    else:
        if len(cms_id)!=6:
                message_else = cms_id+' is an invalid CMS ID.\nPlease enter a valid CMS for enrollment.'
                tkinter.messagebox.showerror('INVALID CMS ID', message_else)
        else:
                tkinter.messagebox.showerror('INVALID ENTRIES', 'Enter the student name to be enrolled.')

#add_student('cs114','Abdullah heelooeoe','291276')

