import datetime as dt

now = dt.datetime.now() # gets the current time

year = now.year

dob = dt.datetime(year=2000, month=3, day=12)
print(dob)