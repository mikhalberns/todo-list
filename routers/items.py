from typing import Optional, Dict, List

from fastapi import APIRouter, status

from db_utils.models import Item
from repository import items

router = APIRouter(
    tags=["items"],
    prefix="/items"
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_item(item: Item) -> Dict[str, str]:
    return items.create_item(item)


@router.get("/{item_task}")
def read_item(item_task: str) -> Dict[str, str]:
    return items.read_item(item_task)


@router.get("/")
def read_items(user: Optional[str] = None, tags: Optional[str] = None) -> List[str]:
    return items.read_items(user, tags)


@router.put("/{item_task}", status_code=status.HTTP_202_ACCEPTED)
def update_item(item_task: str, item: Item) -> Dict[str, str]:
    return items.update_item(item_task, item)


@router.delete("/{item_task}")
def delete_item(item_task: str) -> str:
    return items.delete_item(item_task)
