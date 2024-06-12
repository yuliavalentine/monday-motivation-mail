import datetime as dt
import random
import smtplib

MY_EMAIL = "your mail"
MY_PASSWORD = "your password"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open ("quotes.txt", "r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)



    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday\n\n{quote}")