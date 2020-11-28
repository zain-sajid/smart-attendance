import mysql.connector


mydb=mysql.connector.connect(host="192.168.43.44",user="Jawad Ali",passwd="Password@123",database="testdb")

mycursor=mydb.cursor()

mycursor.execute("SELECT 20_Dec_2019 FROM cs_114 WHERE Name='Jawad' AND CMS_ID=123456")
print(mycursor.fetchall())


