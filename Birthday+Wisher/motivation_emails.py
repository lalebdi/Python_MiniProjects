import smtplib
import datetime as dt
import random

my_email = "example@gmail.com"
password = "blah1234"

with open("quotes.txt") as file:
    quotes = file.readlines()
    quote_of_the_day = random.choice(quotes)


day = dt.datetime.now()
send_day = day.day


if send_day == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # this is basically to encrypt emails
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="example@yahoo.com", msg=f"Subject:Testing 123\n\n{quote_of_the_day}")
