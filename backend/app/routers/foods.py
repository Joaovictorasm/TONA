
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Food)
def create_food(food: schemas.FoodCreate, db: Session = Depends(database.get_db)):
    db_food = models.Food(**food.dict())
    db.add(db_food)
    db.commit()
    db.refresh(db_food)
    return db_food

@router.get("/", response_model=List[schemas.Food])
def read_foods(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    foods = db.query(models.Food).offset(skip).limit(limit).all()
    return foods

@router.get("/{food_id}", response_model=schemas.Food)
def read_food(food_id: int, db: Session = Depends(database.get_db)):
    food = db.query(models.Food).filter(models.Food.id == food_id).first()
    if food is None:
        raise HTTPException(status_code=404, detail="Food not found")
    return food
