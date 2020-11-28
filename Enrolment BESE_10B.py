#Enrolment of Students

import mysql.connector

def add_student(course_name):
    database=mysql.connector.connect(host="localhost",user="root",passwd="Password@123",database="Attendance_Management_System")
    mycursor=database.cursor()

    
    
    sql=f"INSERT INTO {course_name} (Name,CMS_ID) VALUES(%s,%s)"
    students_bese_10b=[("Anas Hanif Attas",284611),("Hanif Ali",309196),
                   ("Fatima Tuz Zehra",284892),("Zain Sajid",283593),
                   ("Shehryar Amin",306453),("Hammad Mukhtar",282678),
                   ("Fatima Mujahid",289558),("Altaf Ahmed",314472),
                   ("Muhammad Ahmad",282660),("Muhammad Maaz",283826),
                   ("Hamna Saeed",295150),("Muhammad Omer Qasim",296872),
                   ("Muhammad Shiraz Husnain",298250),("Muhammad Saqib Rasheed",294517),
                   ("Muhammad Talal Jamil",289682),("Muhammad Uzair Hasnain",295175),
                   ("Anam Tariq",282737),("Laiba Ansar",295364),
                   ("Maheen Nisar",283251),("Ehtisham Ali",297363),
                   ("Fahad Ali",283984),("Tanzeela Nazar",312334),
                   ("Abdul Saboor",291905),("Muhammad Ahmad",293884),
                   ("Saira Sarwar",284606),("Muhammad Shahzaib Chaudhary",290549),
                   ("Waniya Jalal",301517),("Abdullah Shafqat",291276),
                   ("Muhammad Bilal",289436),("Muhammad Usman Khalid",283110),
                   ("Talha Mujahid",294758),("Hassan Khawar",290939),
                   ("Mahina Sheikh",293281),("Taimoor Arshad",294035),
                   ("Rana Nameer Hussain Khan",286271),("Jawad Ali Abbasi",285126),
                   ("Ghayoor Ali",286931),("Fazaila Imran",286996),
                   ("Muhammad Talha Khalid",289635),("Syed Ahmed Ibrahim Shah",285018),
                   ("Muhammad Taha Mahmood",321927)]
    mycursor.executemany(sql,students_bese_10b)
    
    database.commit()

course_name=input("Enter Course Name: ")

add_student(course_name)

