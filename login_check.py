#Check for Valid Student Login

import mysql.connector

def check_student(student_name,cms_id):
    database=mysql.connector.connect(host="localhost",user="root",passwd="Password@123",database="Attendance_Management_System")
    mycursor=database.cursor()
    mycursor.execute("SELECT Name,CMS_ID FROM mac_address")
    authentic_credentials=mycursor.fetchall()
    check_student=(f'{student_name}',cms_id)
    print(check_student)
    for i in range(len(authentic_credentials)):
        if(authentic_credentials[i]==check_student):
            check = 1
            print("You are Clear to GO!")
            break
    else:
        check = 0
        print("Invalid Name or CMS ID")
    
    return check
