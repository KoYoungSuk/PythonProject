import smtplib
from email.mime.text import MIMEText
import getpass
s = smtplib.SMTP("smtp.gmail.com", 587)

s.starttls()

#id = input("Input Your Gmail Account: ")

id = input("Input Your GMail Address: ")
pw = getpass.getpass("Input Your GMail App Password: ")

s.login(id, pw) #Gmail App Password

subject = input("MAIL SUBJECT: ")
message = input("MESSAGE CONTEXT: ")

msg = MIMEText(message)
msg['Subject'] = subject

toemail = input("TO: ")
forwardemail = input("FORWARD: ")

s.sendmail(forwardemail, toemail, msg.as_string())

print("Success!")
s.quit()