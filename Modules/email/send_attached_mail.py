# coding=utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = '***'
receiver = '***'
subject = 'python email test'
smtp_server = 'smtp.163.com'
username = '***'
password = '***'

msgRoot = MIMEMultipart('mixed')
msgRoot['Subject'] = 'test message'

# 构造附件
att = MIMEText(open('/Users/1.jpg', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="1.jpg"'
msgRoot.attach(att)

smtp = smtplib.SMTP()
smtp.connect(smtp_server)
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
