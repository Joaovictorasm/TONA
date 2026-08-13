
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# User schemas
class UserBase(BaseModel):
    email: str
    full_name: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    class Config:
        orm_mode = True

# Protocol schemas
class ProtocolBase(BaseModel):
    name: str
    description: Optional[str] = None

class ProtocolCreate(ProtocolBase):
    pass

class Protocol(ProtocolBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        orm_mode = True

# Exercise schemas
class ExerciseBase(BaseModel):
    name: str
    muscle_group: Optional[str] = None
    equipment: Optional[str] = None

class ExerciseCreate(ExerciseBase):
    pass

class Exercise(ExerciseBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

# Food schemas
class FoodBase(BaseModel):
    name: str
    calories_per_100g: float
    protein_per_100g: float
    carbs_per_100g: float
    fat_per_100g: float

class FoodCreate(FoodBase):
    pass

class Food(FoodBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True
