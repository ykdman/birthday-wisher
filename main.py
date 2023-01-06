##################### Hard Starting Project ######################
import smtplib

import pandas as pd
import datetime as dt
import random

MY_EMAIL = "dbsrudejr300@gmail.com"
MY_PASSWORD = "czulbjhkehlazums"

today = dt.datetime.now()
today_tuple = (dt.datetime.now().month, dt.datetime.now().day)

data = pd.read_csv("birthdays.csv")

# DataFrame에서 for 문의 반복 아이템을 튜플(a, b)로 설정 하면 a에 index, b=data row 가 할당된다.
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:

    birthdays_person = birthdays_dict[today_tuple] # data row의 형식을 저장된 Value 값을 가져온다.
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthdays_person["name"]) # birthdays_person 은 Data Row로 저장되기 때문에 Column 호출 가능

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthdays_person["email"],
                msg=f"Subject:Happy Birthday\n\n{contents}"
                            )




