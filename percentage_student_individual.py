import mysql.connector
import math
    
# Calcutating Percentage for the Attendance Record

def calculate_percentage(table_name,student_name,cms_id):
    database=mysql.connector.connect(host="localhost",user="root",passwd="Password@123",database="Attendance_Management_System")

    mycursor=database.cursor()

    mycursor.execute(f"SELECT * FROM {table_name} WHERE Name='{student_name}' AND CMS_ID={cms_id}")
    attendance_record=mycursor.fetchall()
    print(attendance_record)
    total_lectures=len(attendance_record[0])-2
    print(total_lectures)

    presence=0
    for i in range(len(attendance_record[0])):
        
        if(attendance_record[0][i]=="Present"):
            presence+=1
    try:
        percentage=(presence/total_lectures)*100
        percentage = math.ceil(percentage * 100) / 100
        int_percentage = percentage
        print("Percentage Attendance: {}%".format(percentage))
        percentage=str(percentage)+' %'
    except:
        int_percentage = 0
        percentage='0 %'
    return percentage, int_percentage

#calculate_percentage("cs114","Waniya Jalal",'301517')
        
