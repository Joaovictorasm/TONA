
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Protocol)
def create_protocol(protocol: schemas.ProtocolCreate, db: Session = Depends(database.get_db)):
    # In a real app, we would get the current user from auth
    # For now, we'll hardcode a user_id or skip auth for MVP
    # Let's assume we have a default user with id 1
    db_protocol = models.Protocol(**protocol.dict(), owner_id=1)
    db.add(db_protocol)
    db.commit()
    db.refresh(db_protocol)
    return db_protocol

@router.get("/", response_model=List[schemas.Protocol])
def read_protocols(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    protocols = db.query(models.Protocol).offset(skip).limit(limit).all()
    return protocols

@router.get("/{protocol_id}", response_model=schemas.Protocol)
def read_protocol(protocol_id: int, db: Session = Depends(database.get_db)):
    protocol = db.query(models.Protocol).filter(models.Protocol.id == protocol_id).first()
    if protocol is None:
        raise HTTPException(status_code=404, detail="Protocol not found")
    return protocol

@router.post("/{protocol_id}/exercises/{exercise_id}", response_model=schemas.Protocol)
def add_exercise_to_protocol(protocol_id: int, exercise_id: int, db: Session = Depends(database.get_db)):
    protocol = db.query(models.Protocol).filter(models.Protocol.id == protocol_id).first()
    if protocol is None:
        raise HTTPException(status_code=404, detail="Protocol not found")
    exercise = db.query(models.Exercise).filter(models.Exercise.id == exercise_id).first()
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    if exercise not in protocol.exercises:
        protocol.exercises.append(exercise)
        db.commit()
        db.refresh(protocol)
    return protocol

@router.delete("/{protocol_id}/exercises/{exercise_id}", response_model=schemas.Protocol)
def remove_exercise_from_protocol(protocol_id: int, exercise_id: int, db: Session = Depends(database.get_db)):
    protocol = db.query(models.Protocol).filter(models.Protocol.id == protocol_id).first()
    if protocol is None:
        raise HTTPException(status_code=404, detail="Protocol not found")
    exercise = db.query(models.Exercise).filter(models.Exercise.id == exercise_id).first()
    if exercise is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    if exercise in protocol.exercises:
        protocol.exercises.remove(exercise)
        db.commit()
        db.refresh(protocol)
    return protocol

@router.post("/{protocol_id}/foods/{food_id}", response_model=schemas.Protocol)
def add_food_to_protocol(protocol_id: int, food_id: int, db: Session = Depends(database.get_db)):
    protocol = db.query(models.Protocol).filter(models.Protocol.id == protocol_id).first()
    if protocol is None:
        raise HTTPException(status_code=404, detail="Protocol not found")
    food = db.query(models.Food).filter(models.Food.id == food_id).first()
    if food is None:
        raise HTTPException(status_code=404, detail="Food not found")
    if food not in protocol.foods:
        protocol.foods.append(food)
        db.commit()
        db.refresh(protocol)
    return protocol

@router.delete("/{protocol_id}/foods/{food_id}", response_model=schemas.Protocol)
def remove_food_from_protocol(protocol_id: int, food_id: int, db: Session = Depends(database.get_db)):
    protocol = db.query(models.Protocol).filter(models.Protocol.id == protocol_id).first()
    if protocol is None:
        raise HTTPException(status_code=404, detail="Protocol not found")
    food = db.query(models.Food).filter(models.Food.id == food_id).first()
    if food is None:
        raise HTTPException(status_code=404, detail="Food not found")
    if food in protocol.foods:
        protocol.foods.remove(food)
        db.commit()
        db.refresh(protocol)
    return protocol
