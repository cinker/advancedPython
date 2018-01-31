__author__ = 'srv'

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
from datetime import *
path = "/Users/cinker/Downloads/new/prop/"
today = datetime.today()
today_str = today.strftime('%Y%m%d')
yesterday = today - timedelta(days=1)
yesterday_str = yesterday.strftime('%Y%m%d')
# print(yesterday_str)
dirs = os.listdir(path)
files = {}

for file in dirs:
    files[file[0:8]] = file
file_downloading = files[yesterday_str]
# print(file_downloading)

USERNAME = '64146908@qq.com'  # Email Address from the email you want to send an email
PASSWORD = 'otlmnxirvhwybhbe'  # Password
server = smtplib.SMTP('smtp.qq.com')
FROM_ADDR = '64146908@qq.com'
TO_ADDR = '64146908@qq.com'
html = ''

"""
SMTP Server Information
1. Gmail.com: smtp.gmail.com:587
2. Outlook.com: smtp-mail.outlook.com:587
3. Office 365: outlook.office365.com
Please verify your SMTP settings info.
"""

# Function that send email.
def send_mail(username, password, from_addr, to_addrs, msg):
    server = smtplib.SMTP('smtp.qq.com', '587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, msg.as_string())
    server.quit()

msg = MIMEMultipart()

msg['Subject'] = "Hello How are you ?"
msg['From'] = FROM_ADDR
msg['To'] = TO_ADDR

# Attach files to the email
for file in file_downloading.values():

    # Attach HTML to the email
    html += "<li>" + file + "</li>"
    attch_file = MIMEApplication(open(os.path.join(path, file), "rb").read())
    attch_file.add_header('Content-Disposition', 'attachment', filename=file)
    msg.attach(attch_file)

body = MIMEText(html, 'html')
msg.attach(body)
try:
    send_mail(USERNAME, PASSWORD, FROM_ADDR, TO_ADDR, msg)
    print("Email successfully sent to", TO_ADDR)
except smtplib.SMTPAuthenticationError:
    print('SMTPAuthenticationError')
    print("Email not sent to", TO_ADDR)
