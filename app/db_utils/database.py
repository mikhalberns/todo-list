from pymongo import MongoClient

uri = "mongodb://root:pass12345@host.docker.internal:27018"
client = MongoClient(uri)
db = client.todolist
