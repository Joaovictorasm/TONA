
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

# Association tables for many-to-many relationships
protocol_exercises = Table(
    'protocol_exercises',
    Base.metadata,
    Column('protocol_id', Integer, ForeignKey('protocols.id')),
    Column('exercise_id', Integer, ForeignKey('exercises.id'))
)

protocol_foods = Table(
    'protocol_foods',
    Base.metadata,
    Column('protocol_id', Integer, ForeignKey('protocols.id')),
    Column('food_id', Integer, ForeignKey('foods.id'))
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    # Relationships
    protocols = relationship("Protocol", back_populates="owner")

class Protocol(Base):
    __tablename__ = 'protocols'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    # Relationships
    owner = relationship("User", back_populates="protocols")
    exercises = relationship("Exercise", secondary=protocol_exercises, back_populates="protocols")
    foods = relationship("Food", secondary=protocol_foods, back_populates="protocols")

class Exercise(Base):
    __tablename__ = 'exercises'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    muscle_group = Column(String)
    equipment = Column(String)
    # For substitution logic, we might store alternative exercises
    # But for simplicity, we can have a separate table for exercise alternatives
    # However, we'll keep it simple for now.
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    # Relationships
    protocols = relationship("Protocol", secondary=protocol_exercises, back_populates="exercises")

class Food(Base):
    __tablename__ = 'foods'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    calories_per_100g = Column(Float)
    protein_per_100g = Column(Float)
    carbs_per_100g = Column(Float)
    fat_per_100g = Column(Float)
    # For substitution, we might want to find foods with similar macros
    # We'll implement that in the service layer.
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    # Relationships
    protocols = relationship("Protocol", secondary=protocol_foods, back_populates="foods")
