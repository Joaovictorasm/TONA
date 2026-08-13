
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models

# Create tables
models.Base.metadata.create_all(bind=engine)

db = SessionLocal()
# Check if we already have data
if db.query(models.User).count() == 0:
    # Create a default user with plain text password (for MVP only)
    user = models.User(email="admin@example.com", hashed_password="password", full_name="Admin User")
    db.add(user)
    db.commit()
    db.refresh(user)
    print(f"Created user: {user.email}")
else:
    user = db.query(models.User).first()
    print(f"Using existing user: {user.email}")

# Sample exercises
sample_exercises = [
    {"name": "Flexão de Braço", "muscle_group": "Peito", "equipment": "Corpo"},
    {"name": "Agachamento", "muscle_group": "Pernas", "equipment": "Corpo"},
    {"name": "Rosca Direta", "muscle_group": "Bíceps", "equipment": "Barra"},
    {"name": "Desenvolvimento Militar", "muscle_group": "Ombros", "equipment": "Haltere"},
    {"name": "Levantamento Terra", "muscle_group": "Costas", "equipment": "Barra"},
]

for ex in sample_exercises:
    if not db.query(models.Exercise).filter(models.Exercise.name == ex["name"]).first():
        db_exercise = models.Exercise(**ex)
        db.add(db_exercise)
        print(f"Created exercise: {ex['name']}")

# Sample foods
sample_foods = [
    {"name": "Peito de Frango grelhado", "calories_per_100g": 165, "protein_per_100g": 31, "carbs_per_100g": 0, "fat_per_100g": 3.6},
    {"name": "Arroz integral cozido", "calories_per_100g": 111, "protein_per_100g": 2.6, "carbs_per_100g": 23, "fat_per_100g": 0.9},
    {"name": "Batata doce cozida", "calories_per_100g": 76, "protein_per_100g": 1.4, "carbs_per_100g": 18, "fat_per_100g": 0.1},
    {"name": "Ovo cozido", "calories_per_100g": 155, "protein_per_100g": 13, "carbs_per_100g": 1.1, "fat_per_100g": 11},
    {"name": "Aveia em flocos", "calories_per_100g": 389, "protein_per_100g": 16.9, "carbs_per_100g": 66, "fat_per_100g": 6.9},
]

for fd in sample_foods:
    if not db.query(models.Food).filter(models.Food.name == fd["name"]).first():
        db_food = models.Food(**fd)
        db.add(db_food)
        print(f"Created food: {fd['name']}")

db.commit()
db.close()
print("Seed data loaded.")
