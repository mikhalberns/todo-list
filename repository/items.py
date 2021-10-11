from db_utils.database import db
from db_utils.models import Item
from bson.objectid import ObjectId
from typing import Optional, List


def create_item(item: Item):
    new_item_id = str(db.items.insert_one(dict(item)).inserted_id)
    item = db.items.find_one({"_id": ObjectId(new_item_id)})
    item["_id"] = str(item["_id"])
    return item


def read_item(item_id: str):
    item = db.items.find_one({"_id": ObjectId(item_id)})
    item["_id"] = str(item["_id"])
    return item


def read_items(user: Optional[str] = None, tags: Optional[str] = None) -> List[str]:
    user_filter = {}
    if user:
        user_filter['user'] = user
    if tags:
        user_filter['tags'] = tags

    items = []
    for item in db.items.find(user_filter):
        item["_id"] = str(item["_id"])
        items.append(item)
    return items


def update_item(item_id: str, item: Item):
    user_filter = {"_id": ObjectId(item_id)}
    item = {k: v for k, v in dict(item).items() if v is not None}
    updated_item = {"$set": item}
    db.items.update_one(user_filter, updated_item)
    return item


def delete_item(item_id: str):
    deleted_item = {"_id": ObjectId(item_id)}
    db.items.delete_one(deleted_item)
    return "deleted"
