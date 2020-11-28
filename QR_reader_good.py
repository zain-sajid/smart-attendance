import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys
import time
import re
import uuid
import base64
from datetime import date
import mysql.connector
from update_att import update_attendance
from mac_adder import check_add_mac
import tkinter.messagebox

def function(name, cms, course, lecture_count):
    
    global stop
    stop=0

    today = date.today()
    date_today = today.strftime("%d_%m_%Y")

    code=date_today+"-"+course

    mac=(':'.join(re.findall('..', '%012x' % uuid.getnode()))).upper()
        
    # Function for check if the data is present or not
    def checkData(data):
        try:
            data=str(base64.b64decode(data).decode())
            print(data)
            print(code)
        except:
            print('Invalid QR Code !')
            global stop
            stop = 1
        if stop != 1:
            if data==code:
                print("Course Matched.")
                check_add_mac(name,cms,mac,course,lecture_count)
                stop = 1
            else:
                print("Course Not Matched. Please try another QR Code.")
                tkinter.messagebox.showerror('INVALID QR CODE','Course Not Matched. Please try another QR Code.')
                stop = 1
            
    print('Reading...')

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        
        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            checkData(obj.data)
            time.sleep(1)

        cv2.imshow('frame',frame)
        
        # Closing the program when escape key is pressed or attendance is marked.
        if stop==1:
            cv2.destroyAllWindows()
            break
        
        key = cv2.waitKey(1)
        if key == 27:
            cv2.destroyAllWindows()
            break
    

