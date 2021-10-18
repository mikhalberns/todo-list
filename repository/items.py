from typing import Optional, List, Dict

from bson.objectid import ObjectId
from fastapi import HTTPException, status

from db_utils.database import db
from db_utils.models import Item


def create_item(item: Item) -> Dict[str, str]:
    new_item_id = str(db.items.insert_one(dict(item)).inserted_id)
    item = db.items.find_one({"_id": ObjectId(new_item_id)})
    item["_id"] = str(item["_id"])
    return item


def read_item(item_task: str) -> Dict[str, str]:
    item = db.items.find_one({"task": item_task})
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item with task {item_task} not found")
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


def update_item(item_task: str, item: Item) -> Dict[str, str]:
    item_filter = {"task": item_task}
    item = db.items.find_one(item_filter)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item with task {item_task} not found")
    item = {k: v for k, v in dict(item).items() if v is not None}
    updated_item = {"$set": item}
    db.items.update_one(item_filter, updated_item)
    return item


def delete_item(item_task: str) -> str:
    deleted_item = {"task": item_task}
    item = db.items.find_one(deleted_item)
    if not item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"item with task {item_task} not found")
    db.items.delete_one(deleted_item)
    return "deleted"
