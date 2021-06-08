import smtplib
import datetime as dt
import random

file = open("quotes.txt")
contents = file.read()
contents = contents.split("\n")
letter_msg = random.choice(contents)
file.close()

my_email = "houng-wen.wang@aiesec.net"
password = "LRVJGTQD"

now = dt.datetime.now()
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="whwen0528@gmail.com",
                        msg=f"Subject:Motivation letter\n\n{letter_msg}")
connection.close()
