from fastapi import APIRouter, status
from db_utils.models import Item
from typing import Optional
from repository import items


router = APIRouter(
    tags=["items"],
    prefix="/items"
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_item(item: Item):
    return items.create_item(item)


@router.get("/{item_id}")
def read_item(item_id: str):
    return items.read_item(item_id)


@router.get("/")
def read_items(user: Optional[str] = None, tags: Optional[str] = None):
    return items.read_items(user, tags)


@router.put("/{item_id}", status_code=status.HTTP_202_ACCEPTED)
def update_item(item_id: str, item: Item):
    return items.update_item(item_id, item)


@router.delete("/{item_id}")
def delete_item(item_id: str):
    return items.delete_item(item_id)
