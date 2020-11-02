import datetime

current_date = datetime.datetime.now()
print(current_date)

old_date = datetime.datetime(2009, 8, 11)

uid = users.insert({"username" : "Zeno", "date" : current_date})