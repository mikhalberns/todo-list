from db_utils.database import db
from db_utils.models import Item
from bson.objectid import ObjectId
from typing import Optional, List


def create_item(item: Item):
    new_item_id = str(db.items.insert_one(dict(item)).inserted_id)
    item = db.items.find_one({"_id": ObjectId(new_item_id)})
    item["_id"] = str(item["_id"])
    return item


def read_item(item_task: str):
    item = db.items.find_one({"task": item_task})
    item["_id"] = str(item["_id"])
    return dict(item)


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


def update_item(item_task: str, item: Item):
    item_filter = {"task": item_task}
    item = {k: v for k, v in dict(item).items() if v is not None}
    updated_item = {"$set": item}
    db.items.update_one(item_filter, updated_item)
    return item


def delete_item(item_task: str):
    deleted_item = {"task": item_task}
    db.items.delete_one(deleted_item)
    return "deleted"
