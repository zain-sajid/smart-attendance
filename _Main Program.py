from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import tkinter.messagebox
import time
from datetime import date
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector


def display_manual_override():
    global entry2,entry3,entry4,entry5,entry6
    admin_manual_frame=Frame(admin_display_frame, width=650, height=500,bg='#EBF2F8',highlightbackground='black',highlightthickness=4)
    admin_manual_frame.place(x=0,y=0)
    display_label2=Label(admin_manual_frame,text="CMS ID",font=('Segoe UI',14),bg='#EBF2F8')
    display_label2.place(x=100,y=80)
    entry2=Entry(admin_manual_frame, width=41)
    entry2.place(x=331,y=80)
    display_label3=Label(admin_manual_frame,text="Date(dd_mm_yyyy)",font=('Segoe UI',14),bg='#EBF2F8')
    display_label3.place(x=100,y=130)

    global entry3
    entry3 = date.today()
    def get_sel(e):
        global entry3
        entry3 = cal.get_date()

    cal = DateEntry(admin_manual_frame, width=25, background='#116dff',foreground='white', borderwidth=2,font=('',12))
    cal.place(x=331, y=130)
    cal.bind('<<DateEntrySelected>>', get_sel)

    display_label4=Label(admin_manual_frame,text="Course",font=('Segoe UI',14),bg='#EBF2F8')
    display_label4.place(x=100,y=180)

    optionList = ['Fundamentals of Programming', 'Calculus and Analytic Geometry', 'Discrete Mathematics', 'Islamic Studies', 'English', 'Applied Physics']
    global combobox_entry_manual
    combobox_entry_manual='Fundamentals of Programming'
    def handler(event):
        global combobox_entry_manual
        combobox_entry_manual = subjects_menu.get()
    subjects_menu = ttk.Combobox(admin_display_frame,values = optionList, width=25, font=('',12))
    subjects_menu.current(0)
    subjects_menu.bind('<<ComboboxSelected>>', handler)
    subjects_menu.place(x=335, y=180)

    display_label5=Label(admin_manual_frame,text="Status",font=('Segoe UI',14),bg='#EBF2F8')
    display_label5.place(x=100,y=230)

    optionList2 = ["Present","Absent"]
    global combobox_entry_status
    combobox_entry_status='Present'
    def handler(event):
        global combobox_entry_status
        combobox_entry_status = status_menu.get()
    status_menu = ttk.Combobox(admin_display_frame,values = optionList2, width=25, font=('',12))
    status_menu.current(0)
    status_menu.bind('<<ComboboxSelected>>', handler)
    status_menu.place(x=335, y=230)
    display_label6=Label(admin_manual_frame,text="Lecture No.",font=('Segoe UI',14),bg='#EBF2F8')
    display_label6.place(x=100,y=280)
    entry6=Entry(admin_manual_frame, width=41)
    entry6.place(x=331,y=280)
    mark = Button(admin_manual_frame, image=img6, command=get_input,bd=0,bg='#EBF2F8',cursor='hand2')
    mark.place(x=210,y=380)
    global error_match_string
    error_match_string = StringVar()
    error_match_string.set("")
    student_label_error = Label(admin_manual_frame, textvariable=error_match_string, bg='#EBF2F8', fg='red')
    student_label_error.place(x=50 ,y=470)

def get_input():
    import Manual_Override
    import datetime
    cms_id = entry2.get()
    entry2.delete(0,END)
    print(entry3)
    str_entry3 = str(entry3)

    date_date = datetime.datetime.strptime(str_entry3, '%Y-%m-%d').strftime('%d_%m_%Y')
    print(type(date_date))
    date = str(date_date)
    course = combobox_entry_manual
    if course=='Fundamentals of Programming':
        course = 'cs114'
    elif course=='Calculus and Analytic Geometry':
        course = 'math101'
    elif course=='Discrete Mathematics':
        course = 'math161'
    elif course=='English':
        course = 'hu100'
    elif course=='Islamic Studies':
        course = 'hu101'
    elif course=='Applied Physics':
        course = 'phy102'
    att_status = combobox_entry_status
    lec = entry6.get()
    entry6.delete(0,END)
    att_date = date+'_Lec'+lec
    print(att_date)
    try:
        Manual_Override.manual_override(course,att_date,att_status,cms_id)
    except : error_match_string.set("Invalid Information. Please enter the correct info to mark the attendance.")
    
#defining some variables
lecture_count = 0
flag = 0

#frame defination accessed by clicking the button MARK ATTENDANCE in student_portal()    
def display_when_mark_attendance_clicked():
    global attendance_frame
    attendance_frame = Frame(display_frame, width=650, height=500, bg='#EBF2F8',highlightbackground='black',highlightthickness=4)
    attendance_frame.tkraise()
    attendance_frame.pack()
    instruction_label=Label(attendance_frame,text="Select the Subject and \npress the Attendance Logo\nto automatically mark your attendance",font=('Segoe UI',20),bg='#EBF2F8')
    instruction_label.place(x=90,y=50)
    #defining and implementing the COMBOBOX
    optionList = ['Fundamentals of Programming', 'Calculus and Analytic Geometry', 'Discrete Mathematics', 'Islamic Studies', 'English', 'Applied Physics']
    global combobox_entry_student
    combobox_entry_student='Fundamentals of Programming'
    def handler(event):
        global combobox_entry_student
        combobox_entry_student = subjects_menu.get()
    subjects_menu = ttk.Combobox(attendance_frame,values = optionList, width=30, font=('',14))
    subjects_menu.current(0)
    subjects_menu.bind('<<ComboboxSelected>>', handler)
    subjects_menu.place(x=150, y=200)

    global get
    get=Button(attendance_frame,image=img17,bd=0,bg='#EBF2F8', command=QR_scanner, cursor='hand2')
    get.place(x=200,y=310)
    back = Button(attendance_frame, image=img18,command=home,bd=0,bg='#EBF2F8',cursor='hand2')
    back.place(x=360, y=310)

#function activating webcam to SCAN QR CODE
def QR_scanner():
    import QR_reader_good
    name = student_username_entry.get()
    cms = student_password_entry.get()
    cms = str(cms)
    course = combobox_entry_student
    if course=='Fundamentals of Programming':
        course = 'cs114'
    elif course=='Calculus and Analytic Geometry':
        course = 'math101'
    elif course=='Discrete Mathematics':
        course = 'math161'
    elif course=='English':
        course = 'hu100'
    elif course=='Islamic Studies':
        course = 'hu101'
    elif course=='Applied Physics':
        course = 'phy102'
    QR_reader_good.function(name, cms, course, lecture_count)
        
#frame defination accessed by clicking the button GENERATE QR CODE in admin_portal()
def display_when_generate_qr_code_clicked():
    admin_record_frame=Frame(admin_display_frame, width=650, height=500,bg='#EBF2F8',highlightbackground='black',highlightthickness=4)
    admin_record_frame.place(x=0,y=0)
    display_label=Label(admin_record_frame,text="Choose the subject\nfor which QR Code will be generated",font=('Segoe UI',20),bg='#EBF2F8')
    display_label.place(x=100,y=70)
    optionList = ['Fundamentals of Programming', 'Calculus and Analytic Geometry', 'Discrete Mathematics', 'Islamic Studies', 'English', 'Applied Physics']
    global combobox_entry_admin
    combobox_entry_admin='Fundamentals of Programming'
    def handler(event):
        global combobox_entry_admin
        combobox_entry_admin = subjects_menu.get()
    subjects_menu = ttk.Combobox(admin_record_frame,values = optionList, width=30, font=('',14))
    subjects_menu.current(0)
    subjects_menu.bind('<<ComboboxSelected>>', handler)
    subjects_menu.place(x=150, y=200)
    def entered(event):
        done_button.config(image=img57)
    def left(event):
        done_button.config(image=img56)
    done_button=Button(admin_record_frame,image=img56,command=QR_generator,bd=0,bg='#EBF2F8',cursor='hand2')
    done_button.bind('<Enter>',entered)
    done_button.bind('<Leave>',left)
    done_button.place(x=270,y=340)

#function making a .PNG QR CODE
def QR_generator():
    import QR_generator_good
    import Attendance_Column_Creator
    import mac_address_reset
    mac_address_reset.reset_mac()
    course = combobox_entry_admin
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
    global course_in_append_absent
    course_in_append_absent = course
    lecture = 1
    date1 = date.today()
    current_date = date1.strftime('%d_%m_%Y')
    global lecture_count
    lecture_count = Attendance_Column_Creator.attendance_column(course, current_date)

    lecture=str(lecture)
    QR_generator_good.function_generator(course)
    time.sleep(2)
    display_after_qr_code_generated()

def display_after_qr_code_generated():
    global count_how_many_times_appended
    showrecord_frame_qr=Frame(admin_display_frame, width=650, height=500,bg='#EBF2F8',highlightbackground='black',highlightthickness=4)
    showrecord_frame_qr.place(x=0,y=0)
    showrecord_frame_qr.tkraise()
    global img69
    img69 = PhotoImage(file="QRcodeImg.png") 
    qr_code_label = Label(showrecord_frame_qr,image=img69, relief='raised')
    qr_code_label.place(x=140, y=30)
    def entered(event):
        done_button.config(image=img57)
    def left(event):
        done_button.config(image=img56)
    done_button =Button(showrecord_frame_qr,image=img56,bd=0,bg='#EBF2F8',command=this_will_append_absents,cursor='hand2')
    done_button.bind('<Enter>',entered)
    done_button.bind('<Leave>',left)
    done_button.place(x=270,y=420)

def this_will_append_absents():
    import Append_Absent
    date1 = date.today()
    current_date = date1.strftime('%d_%m_%Y')
    Append_Absent.append_absent(course_in_append_absent,lecture_count)
    admin_portal()


get=None


student_login_frame=None
student_password_entry=None
student_username_entry=None

def student_login():
    global student_login_frame
    student_login_frame = Frame(student_admin_frame, width=900, height=500, bg='#EBF2F8')
    student_login_frame.place(x=0, y=0)
    student_login_frame.tkraise()
    student_icon = Label(student_login_frame, image=img15, bd=0, bg='#EBF2F8')
    student_icon.place(x=370, y=10)
    username_label = Label(student_login_frame, text='Full Name', font=('Berlin Sans FB', 16), bg='#EBF2F8')
    username_label.place(x=405, y=200)
    global student_username_entry
    student_username_entry = Entry(student_login_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    student_username_entry.place(x=350, y=240)
    password_label = Label(student_login_frame, text='CMS ID', font=('Berlin Sans FB', 16), bg='#EBF2F8')
    password_label.place(x=415, y=280)
    global student_password_entry
    student_password_entry = Entry(student_login_frame, bg='white', show='*', relief='sunken', highlightcolor='#D2E0F1',highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    student_password_entry.place(x=350, y=320)
    student_password_entry.bind('<Return>', authorize)
    #a label for giving message that the password and username dont match
    global error_match_string
    error_match_string = StringVar()
    error_match_string.set("")
    student_label_error = Label(student_login_frame, textvariable=error_match_string, bg='#EBF2F8', fg='red')
    student_label_error.place(x=260 ,y=355)
    
    login_button = Button(student_login_frame, image=img24, bd=0, bg='#EBF2F8', cursor='hand2')
    login_button.bind('<Button-1>',authorize)
    login_button.place(x=357, y=380)
    cancel_button = Button(student_login_frame, image=img14, bd=0, bg='#EBF2F8', command=student_exit, cursor='hand2')
    cancel_button.place(x=357, y=430)


def authorize(event):
    import login_check
    global flag
    flag = 0
    try:
        student_password_entry_float = float(student_password_entry.get())
        flag = login_check.check_student(student_username_entry.get(), int(student_password_entry_float))
        if flag==1:
            student_portal()
        else : error_match_string.set("The user name or CMS ID that you've entered doesn't match any account.")

    except:
        flag = 0
        error_match_string.set("The user name or CMS ID that you've entered doesn't match any account.")

var3=None
enter_data_entry=None

def home():
    global display_frame
    display_frame = Frame(student_login_frame, width=650, height=500, bg='#EBF2F8',highlightbackground='black',highlightthickness=4)
    display_frame.place(x=250, y=0)
    display_frame.tkraise()

var2=None
attendance_frame=None

display_frame=None
dashboard_button_1=None
def student_portal():
    dashboard_frame=Frame(student_login_frame,width=250,height=500,bg='#FFFFFF',highlightbackground='black',highlightthickness=4)
    dashboard_frame.place(x=0,y=0)
    dashboard_frame.tkraise()
    dashboard_label=Label(dashboard_frame,image=img5,bg='#FFFFFF')
    dashboard_label.place(x=15,y=5)
    global dashboard_button_1
    #button taking attnedance taking you to QR SCANNER for marking attendace
    dashboard_button_1 = Button(dashboard_frame,image=img6,command=display_when_mark_attendance_clicked,bg='#FFFFFF',bd=0,cursor='hand2')
    dashboard_button_1.place(x=6, y=120)
    #button taking you to popup window showing database in a table
    dashboard_button_2 = Button(dashboard_frame, image=img50,bd=0,bg='#FFFFFF', command=show_student_record,cursor='hand2')
    dashboard_button_2.place(x=6, y=170)
    def entered(event):
        dashboard_button_3.config(image=img52)
    def left(event):
        dashboard_button_3.config(image=img8)
    dashboard_button_3 = Button(dashboard_frame, image=img8,bd=0,bg='#FFFFFF', command=student_login,cursor='hand2')
    dashboard_button_3.bind('<Enter>', entered)
    dashboard_button_3.bind('<Leave>', left)
    dashboard_button_3.place(x=6, y=440)

    global display_frame
    display_frame=Frame(student_login_frame,width=650,height=500,bg='#EBF2F8')
    display_frame.place(x=250,y=0)
    display_frame.tkraise()

def show_student_record():
    import percentage_student_individual
    showrecord_frame=Frame(display_frame, width=650, height=500,bg='#EBF2F8', highlightbackground='black',highlightthickness=4)
    showrecord_frame.place(x=0,y=0)
    showrecord_frame.tkraise()
    name = student_username_entry.get()
    cms = student_password_entry.get()

    try:
        cs144_percentage, cs144_percentage_int = percentage_student_individual.calculate_percentage('cs114',name,cms)
        cs144_label=Label(showrecord_frame,text=cs144_percentage,font=('Segoe UI',20))
        cs144_label.place(x=450, y=20)
        cs144_description=Label(showrecord_frame,text="Attendance Percentage CS-114\nFundamentals of Programming",font=('Segoe UI',14))
        cs144_description.place(x=100,y=20)
        warning = 0
        if cs144_percentage_int<75:
            warning = 1
    except:
        #cs144_description=Label(showrecord_frame,text="A place holder for attendance\nof another course",font=('Segoe UI',14))
        #cs144_description.place(x=100,y=20)
        pass

    try:
        hu100_percentage, hu100_percentage_int = percentage_student_individual.calculate_percentage('hu100',name,cms)
        hu100_label=Label(showrecord_frame,text=hu100_percentage,font=('Segoe UI',20))
        hu100_label.place(x=450, y=95)
        hu100_description=Label(showrecord_frame,text="Attendance Percentage HU-100\nEnglish",font=('Segoe UI',14))
        hu100_description.place(x=100,y=95)

        if hu100_percentage_int<75:
            warning = 1
    except:
        pass

    try:
        hu101_percentage, hu101_percentage_int = percentage_student_individual.calculate_percentage('hu101',name,cms)
        hu101_label=Label(showrecord_frame,text=hu101_percentage,font=('Segoe UI',20))
        hu101_label.place(x=450, y=170)
        hu101_description=Label(showrecord_frame,text="Attendance Percentage HU-101\nIslamic Studies",font=('Segoe UI',14))
        hu101_description.place(x=100,y=170)

        if hu101_percentage_int<75:
            warning = 1
    except:
        pass

    try:
        math161_percentage, math161_percentage_int = percentage_student_individual.calculate_percentage('math161',name,cms)
        math161_label=Label(showrecord_frame,text=math161_percentage,font=('Segoe UI',20))
        math161_label.place(x=450, y=245)
        math161_description=Label(showrecord_frame,text="Attendance Percentage MATH-161\nDiscrete Mathematics",font=('Segoe UI',14))
        math161_description.place(x=100,y=245)

        if math161_percentage_int<75:
            warning = 1
    except:
        pass

    try:
        math101_percentage, math101_percentage_int = percentage_student_individual.calculate_percentage('math101',name,cms)
        math101_label=Label(showrecord_frame,text=math101_percentage,font=('Segoe UI',20))
        math101_label.place(x=450, y=320)
        math101_description=Label(showrecord_frame,text="Attendance Percentage MATH-101\nCalculus and Analytical Geometry",font=('Segoe UI',14))
        math101_description.place(x=100,y=320)

        if math101_percentage_int<75:
            warning = 1
    except:
        pass

    try:
        phy102_percentage, phy102_percentage_int = percentage_student_individual.calculate_percentage('phy102',name,cms)
        phy102_label=Label(showrecord_frame,text=phy102_percentage,font=('Segoe UI',20))
        phy102_label.place(x=450, y=395)
        phy102_description=Label(showrecord_frame,text="Attendance Percentage PHY-102\nApplied Physics",font=('Segoe UI',14))
        phy102_description.place(x=100,y=395)

        if phy102_percentage_int<75:
            warning = 1
    except:
        pass

    if warning==1:
        tkinter.messagebox.showwarning('SHORT ATTENDANCE', 'Your Attendance is below the required 75% in a course, consider attending more classes')

    back = Button(showrecord_frame, image=img18,command=home,bd=0,bg='#EBF2F8',cursor='hand2')
    back.place(x=550, y=200)

#def loading_data2():
    #loading_data(combobox_entry_admin_records)

def loading_data(course_tag):
    import tkinter as tk
    from tkinter import ttk

    course = course_tag
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

    #this here gives all the column names and the entries in the database file
    def course_records(table_name):
        database=mysql.connector.connect(host="localhost",user="root",passwd="Password@123",database="Attendance_Management_System")
        mycursor=database.cursor()

        mycursor.execute(f"SELECT COLUMN_NAME FROM information_schema.COLUMNS WHERE TABLE_NAME='{table_name}' ORDER BY ORDINAL_POSITION")
        column_titles=mycursor.fetchall()

        mycursor.execute(f"SELECT * FROM {table_name} ORDER BY Name")
        records=mycursor.fetchall()
        return records, column_titles

    #calling the function with table_name='math161'
    records, column_titles = course_records(course)

    #this for loop generates the column names into a single tuple for use later stored in main_tuple
    #also a counter is generated to count no of columns in database 
    main_tuple = ()
    tuple_no_elements = 0
    for outer in column_titles:
        for inner in outer:
            ok_tuple = tuple([inner])
            main_tuple = main_tuple+ok_tuple
            tuple_no_elements = tuple_no_elements + 1

    #setting a variable so that the same table does not load stuff twice
    #global table_set_once_check
    #table_set_once_check = 0


    #loading data into a table with columns generated already
    def show():
        #this for loop generates a list of the form ['date0'.'date1', till no of columns]
        variable_dates=[]
        for count in range(tuple_no_elements):
            date_var = 'date'
            date_var = date_var + str(count)
            variable_dates = variable_dates+[date_var]
        
        tempList = records
        
        #a loop for turning variable_dates from a list to a string of form ('date0','date1' till end)
        string=''
        for count in variable_dates:
            if string=='':
                string = count
            else : string = string+','+count 
        string = '('+string+')'
        
        #looping through the records from database and printing them accordingly in rows and columns
        for i, string in enumerate(records, start=1):
            treeview.insert('', "end", values=string)
            

    #defining the tkinter main window
    table_pop = tk.Tk()
    table_pop.geometry('900x500')
    table_pop.title('Records Table')
    table_pop.iconbitmap('favicon.ico')
    table_pop.resizable(0, 0) 

    #making a treeview with columns equaling in database
    treeview = ttk.Treeview(table_pop, columns=main_tuple, show='headings')

    #set column headings
    #count for making first column width bigger than others 
    count = 0
    for col in main_tuple:
        count = count + 1
        treeview.heading(col, text=col)
        print(col)
        if count==1:
        	treeview.column(col,width=170, stretch=NO)
        else: treeview.column(col,width=100, stretch=NO)

    treeview.pack(fill='both',side='left', expand=1)

    vsb = ttk.Scrollbar(table_pop, orient="vertical", command=treeview.yview)
    vsb.pack(side='right', fill='y')

    hsb = ttk.Scrollbar(treeview, orient="horizontal", command=treeview.xview)
    hsb.pack(side='bottom', fill='x')

    treeview.config(xscrollcommand=hsb.set, yscrollcommand=vsb.set)

    show()

    table_pop.mainloop()

def show_admin_record():
    show_admin_record_frame = Frame(admin_display_frame, width=650, height=500, bd=0, bg='#EBF2F8')
    show_admin_record_frame.place(x=0, y=0)
    show_admin_record_frame.tkraise()

    global combobox_entry_admin_records
    combobox_entry_admin_records = 'Fundamentals of Programming'

    def handler(event):
        global combobox_entry_admin_records
        combobox_entry_admin_records = combobox_show_admin_record.get()
        print(combobox_entry_admin_records)

    optionList = ['Fundamentals of Programming', 'Calculus and Analytic Geometry', 'Discrete Mathematics', 'Islamic Studies', 'English', 'Applied Physics']
    
    combobox_show_admin_record = ttk.Combobox(show_admin_record_frame,values = optionList, width=30, font=('',14))
    combobox_show_admin_record.current(0)
    combobox_show_admin_record.bind('<<ComboboxSelected>>', handler)
    combobox_show_admin_record.place(x=150, y=150)

    button_show_record_admin = Button(show_admin_record_frame, text='Generate Student Attendance For Chosen Subject', command=lambda: loading_data(combobox_entry_admin_records), font=('Segoe UI',12), bg='#116dff',fg='#FFFFFF')
    button_show_record_admin.place(x=150, y=250)

admin_display_frame=None

def enrolling_student():
    import Student_Enrollment
    show_enrolling_frame = Frame(admin_display_frame, width=650, height=500, bd=0, bg='#EBF2F8')
    show_enrolling_frame.place(x=0, y=0)
    show_enrolling_frame.tkraise()
    display_label1=Label(show_enrolling_frame,text="Name",font=('Segoe UI',14),bg='#EBF2F8')
    display_label1.place(x=100,y=80)
    entry1=Entry(show_enrolling_frame,width=41)
    entry1.place(x=360, y=80)
    display_label2=Label(show_enrolling_frame,text="CMS ID",font=('Segoe UI',14),bg='#EBF2F8')
    display_label2.place(x=100,y=140)
    entry2=Entry(show_enrolling_frame,width=41)
    entry2.place(x=360,y=140)

    global combobox_entry_enrolling
    combobox_entry_enrolling = 'Fundamentals of Programming'

    def handler(event):
        global combobox_entry_enrolling
        combobox_entry_enrolling = combobox_enrolling.get()
        print(combobox_entry_enrolling)
    optionList = ['Fundamentals of Programming', 'Calculus and Analytic Geometry', 'Discrete Mathematics', 'Islamic Studies', 'English', 'Applied Physics']
    display_label3=Label(show_enrolling_frame,text="Course",font=('Segoe UI',14),bg='#EBF2F8')
    display_label3.place(x=100,y=200)    
    combobox_enrolling = ttk.Combobox(show_enrolling_frame,values = optionList, width=25, font=('',12))
    combobox_enrolling.current(0)
    combobox_enrolling.bind('<<ComboboxSelected>>', handler)
    combobox_enrolling.place(x=360, y=200)
    def entered(event):
        done_button.config(image=img57)
    def left(event):
        done_button.config(image=img56)
    done_button=Button(show_enrolling_frame,image=img56,command=lambda: Student_Enrollment.add_student(combobox_entry_enrolling,entry1.get(),entry2.get()),bd=0,bg='#EBF2F8',cursor='hand2')
    done_button.bind('<Enter>',entered)
    done_button.bind('<Leave>',left)
    done_button.place(x=270,y=340)

#hover function

def admin_portal():
    admin_dashboard_frame = Frame(admin_login_frame, width=250, height=500, bg='#FFFFFF',highlightbackground='black',highlightthickness=4)
    admin_dashboard_frame.place(x=0, y=0)
    admin_dashboard_frame.tkraise()
    dashboard_label = Label(admin_dashboard_frame, image=img5, bg='#FFFFFF')
    dashboard_label.place(x=15, y=5)
    #generate QR code button
    dashboard_button_2 = Button(admin_dashboard_frame, image=img51, bd=0, bg='#FFFFFF', command=display_when_generate_qr_code_clicked,cursor='hand2')
    dashboard_button_2.place(x=6, y=120)
    #Manual Override Button
    dashboard_button_2 = Button(admin_dashboard_frame, image=img58, bd=0, bg='#FFFFFF', command=display_manual_override,cursor='hand2')
    dashboard_button_2.place(x=6, y=170)
    #View Records Button
    dashboard_button_1 = Button(admin_dashboard_frame, image=img7, bd=0, bg='#FFFFFF', command=show_admin_record,cursor='hand2')
    dashboard_button_1.place(x=6, y=220)
    #Enroll Student Button
    dashboard_button_4 = Button(admin_dashboard_frame, image=img59, bd=0, bg='#FFFFFF', command=enrolling_student, cursor='hand2')
    dashboard_button_4.place(x=6, y=270)
    #logout button
    def entered(event):
        dashboard_button_3.config(image=img52)
    def left(event):
        dashboard_button_3.config(image=img8)
    dashboard_button_3 = Button(admin_dashboard_frame, image=img8, bd=0, bg='#FFFFFF', command=admin_login,cursor='hand2')
    dashboard_button_3.bind('<Enter>', entered)
    dashboard_button_3.bind('<Leave>', left)
    dashboard_button_3.place(x=6, y=440)
    global admin_display_frame
    admin_display_frame = Frame(admin_login_frame, width=650, height=500,bg='#EBF2F8', highlightbackground='black',highlightthickness=4)
    admin_display_frame.place(x=250, y=0)
    admin_display_frame.tkraise()

def admin_authorize(event):

    if admin_username_entry.get()=='admin' and admin_password_entry.get()=='password':
        error_match_string2.set('')
        admin_portal()
    else :
        error_match_string2.set("The user name or password that you've entered doesn't match any account.")


def student_exit():
    main_window()


def admin_exit():
    main_window()

admin_username_entry=None
admin_password_entry=None
admin_login_frame=None

def admin_login():
    global admin_login_frame
    admin_login_frame=Frame(student_admin_frame,width=900,height=500,bg='#EBF2F8')
    admin_login_frame.place(x=0,y=0)
    admin_login_frame.tkraise()
    admin_icon=Label(admin_login_frame,image=img13,bd=0,bg='#EBF2F8')
    admin_icon.place(x=370,y=10)
    username_label=Label(admin_login_frame,text='Username',font=('Berlin Sans FB',16),bg='#EBF2F8')
    username_label.place(x=405,y=200)
    global admin_username_entry
    admin_username_entry=Entry(admin_login_frame,bg='white',relief='sunken',highlightcolor='#D2E0F1',highlightthickness=1,highlightbackground='#D8D6D7',font=('Tw Cen MT',14))
    admin_username_entry.place(x=350,y=240)
    password_label = Label(admin_login_frame, text='Password', font=('Berlin Sans FB', 16), bg='#EBF2F8')
    password_label.place(x=405, y=280)
    global admin_password_entry
    admin_password_entry = Entry(admin_login_frame, bg='white',show='*', relief='sunken', highlightcolor='#D2E0F1',highlightthickness=1,highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    admin_password_entry.place(x=350, y=320)
    admin_password_entry.bind('<Return>',admin_authorize)
    #a label for giving message that the password and username dont match
    global error_match_string2
    error_match_string2 = StringVar()
    error_match_string2.set("")
    admin_label_error = Label(student_login_frame, textvariable=error_match_string2, bg='#EBF2F8', fg='red')
    admin_label_error.place(x=260 ,y=355)

    login_button=Button(admin_login_frame,image=img24,bd=0,bg='#EBF2F8',cursor='hand2')
    login_button.bind('<Button-1>',admin_authorize)
    login_button.place(x=357,y=380)
    cancel_button=Button(admin_login_frame,image=img14,bd=0,bg='#EBF2F8',command=admin_exit,cursor='hand2')
    cancel_button.place(x=357,y=430)


student_admin_frame=None

def main_window():
    def entered1(event):
        black_button_student.config(image=img55)
    def left1(event):
        black_button_student.config(image=img11)
    def entered2(event):
        black_button_teacher.config(image=img54)
    def left2(event):
        black_button_teacher.config(image=img12)

    global student_admin_frame
    student_admin_frame = Frame(root, width=900, height=500,bg="#212b31")
    student_admin_frame.place(x=0, y=0)
    main_logo_image=Label(student_admin_frame,image=img23,bg='#EBF2F8')
    main_logo_image.place(x=200,y=50)
    black_button_student = Button(student_admin_frame,image=img11, bd=0,activebackground='#212b31', command=student_login,bg="#212b31", cursor='hand2')
    black_button_student.place(x=205, y=350)
    black_button_student.bind('<Enter>',entered1)
    black_button_student.bind('<Leave>',left1)
    black_button_teacher = Button(student_admin_frame,image=img12, bd=0,activebackground='#212b31', command=admin_login,bg="#212b31", cursor='hand2')
    black_button_teacher.bind('<Enter>',entered2)
    black_button_teacher.bind('<Leave>',left2)
    black_button_teacher.place(x=505, y=350)

root=Tk()
root.geometry("900x500")
root.title("Smart Attendance")
root.resizable(0,0)
root.iconbitmap('favicon.ico')
img5=PhotoImage(file='Templates\\button_menu1.png')
img6=PhotoImage(file='Templates\\button_mark_attendance5.png')
img7=PhotoImage(file='Templates\\button_view_records5.png')
img8=PhotoImage(file='Templates\\button_logout.png')
img11=PhotoImage(file='Templates\\button_student2.png')
img12=PhotoImage(file='Templates\\button_admin2.png')
img23=PhotoImage(file='Templates\\whatshouldiname.png')
img24=PhotoImage(file='Templates\\login-button.png')
img13=PhotoImage(file='Templates\\admin_picture.png')
img14=PhotoImage(file='Templates\\cancel-button.png')
img15=PhotoImage(file='Templates\\student_picture.png')
img17=PhotoImage(file='Templates\\button_attendance_logo.png')
img18=PhotoImage(file='Templates\\button_back_icon.png')
img50=PhotoImage(file='Templates\\button_%5.png')
img51=PhotoImage(file='Templates\\button_generate_qr_code5.png')
img52=PhotoImage(file='Templates\\button_logout2.png')
img54=PhotoImage(file='Templates\\button_admin3.png')
img55=PhotoImage(file='Templates\\button_student3.png')
img56=PhotoImage(file='Templates\\button_done.png')
img57=PhotoImage(file='Templates\\button_done2.png')
img58=PhotoImage(file='Templates\\button_manual_attendance.png')
img59=PhotoImage(file='Templates\\button_enroll_student.png')
main_window()

root.mainloop()
