from pymongo import MongoClient


client = MongoClient(port=27018)
db = client.todolist
