from pymongo import MongoClient

uri = "mongodb://root:pass12345@localhost:27018/?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false"
client = MongoClient(uri)
db = client.todolist
