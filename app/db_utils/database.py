from pymongo import MongoClient
from ..config import conf

uri = f"mongodb://{conf.get_db_user()}:{conf.get_db_user_pass()}@{conf.get_db_host()}:{conf.get_db_port()}"

client = MongoClient(uri)
db = client.todolist
