from db_utils.database import db
from db_utils.models import Item
from bson.objectid import ObjectId
from typing import Optional


def create_item(item: Item):
    new_item = str(db.items.insert_one(dict(item)).inserted_id)
    item = db.items.find_one({"_id": ObjectId(new_item)})
    item["_id"] = str(item["_id"])
    return item


def read_item(item_id: str):
    item = db.items.find_one({"_id": ObjectId(item_id)})
    item["_id"] = str(item["_id"])
    return item


def read_items(user: Optional[str] = None, tags: Optional[str] = None):
    user_filter = {}
    if user:
        user_filter = {"user": user}
    if tags:
        user_filter = {"tags": tags}
    if user and tags:
        user_filter = {"user": user, "tags": tags}
    items = []
    for item in db.items.find(user_filter):
        item["_id"] = str(item["_id"])
        items.append(item)
    return items


def update_item(item_id: str, item: Item):
    user_filter = {"_id": ObjectId(item_id)}
    item = {k: v for k, v in dict(item).items() if v is not None}
    update_item = {"$set": item}
    db.items.update_one(user_filter, update_item)
    return item


def delete_item(item_id: str):
    delete_item = {"_id": ObjectId(item_id)}
    db.items.delete_one(delete_item)
    return "deleted"
