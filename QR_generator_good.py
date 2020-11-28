from MyQR import myqr
import os
import base64
from datetime import date

def function_generator(course):
    
    today = date.today()
    date_today = today.strftime("%d_%m_%Y")
    code=date_today+"-"+course

    print("Generating...")

    with open("data.txt","w") as f:
        f.write(code)

    with open('data.txt','r') as f:
        lines = f.read().split("\n")
        
    for i in range(0,len(lines)):
        data=lines[i].encode('utf-8')
        name=(base64.b64encode(data).decode())
        version, level, qr_name = myqr.run(
        str(name),
        version = 1,
        level = 'H',
        picture = '',
        colorized = True,
        contrast = 1.0,
        brightness = 1.0,
        save_name = str('QRcodeImg.png'),
        save_dir = os.getcwd()
        )

    print("Generated Successfully.")

