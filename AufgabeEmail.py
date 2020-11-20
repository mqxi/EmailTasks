# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:17:35 2020

@author: Maxi
"""
import smtplib, ssl, email

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime

timeNow = datetime.datetime.now() # date and time for the subject
sender_email = "" #enter your email 
receiver_email = "" #enter the receiver email
#password = input("Type your password and press enter: ")
datei = open("password.txt",'r') # opens a txt file which contains 
password = datei.readline() #read the password
datei.close # close the file

message = MIMEMultipart() # multipart needed for html, text and attachment together
message["Subject"] = f"Programmierung vom {timeNow}"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version message
text = """\
Hi,
Was machst du grade?
Im Anhang erhälst du eine Datei.

Grüße
dein E-Mail Bot
"""

html = """\
<html>
    <body>
        <p>
            Hi,
        <br>
            Was machst du grade?
        <br>
            Im Anhang erhälst du eine Datei.
        <br>
        <br>
            Grüße
        <br>
            dein E-Mail Bot
        </p>
    </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

file = "document.pdf" #attachment 

attach_file = open(file, "rb") # open the file
part3 = MIMEBase("application", "octate-stream")
part3.set_payload((attach_file).read())
encoders.encode_base64(part3) # encode the file into ASCII characters
part3.add_header('Content-Disposition', 'attachment', filename=file)
# Add attachment part to MIMEMultipart objects
message.attach(part3)



# Create secure connection with server and send email
context = ssl.create_default_context()
# SMTP and Port of your web server
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
# confirmation
print('sent!')
