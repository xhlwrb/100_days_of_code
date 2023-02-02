# import smtplib
#
# my_email = "100daysg@gmail.com"
# password = "gfjzvlmufwfzjkla"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="yh100days@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of your email."
#                         )
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# print(now)
# print(year)
# print(type(year))
# print(type(now))
#
# date_of_birth = dt.datetime(year=1994, month=12, day=30)
# print(date_of_birth)
import smtplib
import random
import datetime as dt

my_email = "100daysg@gmail.com"
password = "gfjzvlmufwfzjkla"

now = dt.datetime.now()
weekday = now.weekday()
weekday = 1

if weekday == 1:
    with open("quotes.txt") as data_file:
        quotes = data_file.read().splitlines()
        random_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Monday Motivation\n\n{random_quote}"
                            )


