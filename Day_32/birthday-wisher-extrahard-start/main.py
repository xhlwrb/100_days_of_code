##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import pandas as pd
import random

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

birthday_data = pd.read_csv("birthdays.csv")
birthday_list = birthday_data.to_dict(orient="records")
today = dt.datetime.now()
my_email = "100daysg@gmail.com"
my_password = "gfjzvlmufwfzjkla"

letter_modules = []
with open("letter_templates\\letter_1.txt") as data_file:
    letter_modules.append(data_file.read())
with open("letter_templates\\letter_2.txt") as data_file:
    letter_modules.append(data_file.read())
with open("letter_templates\\letter_3.txt") as data_file:
    letter_modules.append(data_file.read())


for person in birthday_list:
    if person["year"] == today.year and person["month"] == today.month and person["day"] == today.day:
        send_name = person["name"]
        random_letter = random.choice(letter_modules)
        random_letter = random_letter.replace("[NAME]", send_name)

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=person["email"],
                                msg=f"Subject:Happy Birthday!\n\n{random_letter}")


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.






