import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()
server.login('bhanurajpoot2008@gmai.com', 'test@123')

server.sendmail('bhanurajpoot2008@gmail.com', 'reciever@gmail.com', 'Hi, This is testing mail.')

print('Mail sent.')