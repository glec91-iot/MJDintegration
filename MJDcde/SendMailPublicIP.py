import smtplib
from requests import get

ip = get('http://api.ipify.org').text 
to = 'gleclercq91@gmail.com'
gmail_user = 'gleclercq91@gmail.com'
gmail_pwd ='xxxxxxx'
smtpserver = smtplib.SMTP("smtp.gmail.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:@pi \n'
msg = header + '\n @pi='+ ip  +'\n\n'
print msg
smtpserver.sendmail(gmail_user, to, msg)
print 'done!'
smtpserver.close()
