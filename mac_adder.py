#Adding Mac Addresses to the Database and Preventing Duplicates
import mysql.connector
from update_att import update_attendance
import tkinter


def check_add_mac(name,cms_id,mac_address,course,date):
    database=mysql.connector.connect(host="localhost",user="root",passwd="Password@123",database="Attendance_Management_System")
    mycursor=database.cursor()

    mycursor.execute("SELECT Mac_Addresses FROM Mac_Address")
    address_list=mycursor.fetchall()
    
    mac_original=mac_address
    mac_address=(f'{mac_address}',)
    
    for i in range(len(address_list)):
        if(mac_address == address_list[i]):
            tkinter.messagebox.showerror('ERROR', 'Device has already been used.')
            print("Device has already been used.")
            break
    else:
        mycursor.execute(f"UPDATE Mac_Address SET Mac_Addresses='{mac_original}' WHERE Name='{name}' AND CMS_ID={cms_id}")
        update_attendance(course,date,name,cms_id)
        print('Marked Present in',course)
    
    database.commit()
    
    
