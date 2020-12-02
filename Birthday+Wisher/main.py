import smtplib

my_email = "example@gmail.com"
password = "blah1234"

# sometimes for this to work you need to lower the security settings (allow low security apps)

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls() # this is basically to encrypt emails
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="example@yahoo.com", msg="Subject:Testing 123\n\nThis is the body of my email")

connection.close()

# or:

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() # this is basically to encrypt emails
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="example@yahoo.com", msg="Subject:Testing 123\n\nThis is the body of my email")
