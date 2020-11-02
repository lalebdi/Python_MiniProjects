import pymongo
from pymongo import MongoClient

myClient = MongoClient()
db = myClient.mydb

users = db.users

user1 = {"username":"Leah", "password" : "macbook", "favorite_number" : 9, "hobbies" : ["python", "running", "pizza"]}

user_id = users.insert_one(user1).inserted_id

user_id