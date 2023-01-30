import smtplib as s

obj = s.SMTP('smptp.gmail.com', 587)
obj.ehlo()
obj.starttls()
obj.login("sender_add@gmail.com", "pass123")
subject = "test python"
body = "I love Python"
message = "subject:{}\n\n{}".format(subject, body)
listadd = ['receiver_add1@gmail.com',
           'receiver_add2@gmail.com',
           'receiver_add3@gmail.com']
obj.sendmail("sender_add@gmail.com", listadd, message)
print("Sending Mail Successfully!")
obj.quit()