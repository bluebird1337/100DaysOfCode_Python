import datetime as dt
import pandas
import random
import smtplib

my_email = "houng-wen.wang@aiesec.net"
password = "LRVJGTQD"

data = pandas.read_csv("birthdays.csv")
birth_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

today = (dt.datetime.now().month, dt.datetime.now().day)

if today in birth_dict:
    birth_person = birth_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birth_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email, to_addrs=birth_person["email"],
                            msg=f"Subject: Happy Birth day!\n\n{contents}")

