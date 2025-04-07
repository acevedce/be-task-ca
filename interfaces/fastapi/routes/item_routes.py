from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from use_cases.item.create_item import CreateItem
from use_cases.item.get_all_items import GetAllItems
from infrastructure.sqlalchemy.item_repository import SQLAlchemyItemRepository
from infrastructure.inmemory.item_repository import InMemoryItemRepository
from infrastructure.sqlalchemy.db import get_db
from app import USE_IN_MEMORY

router = APIRouter()

in_memory_item_repo = InMemoryItemRepository()

class CreateItemRequest(BaseModel):
    name: str
    description: str
    price: float
    quantity: int

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

@router.post("/items", response_model=ItemResponse)
def create_item(req: CreateItemRequest, db: Session = Depends(get_db)):
    repo = in_memory_item_repo if USE_IN_MEMORY else SQLAlchemyItemRepository(db)
    use_case = CreateItem(repo)
    try:
        item = use_case.execute(**req.dict())
        return item
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.get("/items", response_model=list[ItemResponse])
def get_all_items(db: Session = Depends(get_db)):
    repo = in_memory_item_repo if USE_IN_MEMORY else SQLAlchemyItemRepository(db)
    use_case = GetAllItems(repo)
    return use_case.execute()