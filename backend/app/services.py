
from typing import List, Tuple
from sqlalchemy.orm import Session
from app import models

def find_similar_exercises(db: Session, target_exercise: models.Exercise, limit: int = 5) -> List[models.Exercise]:
    """
    Find exercises that target the same muscle group
    In a more advanced system, we could also consider equipment, movement pattern, etc.
    """
    similar = db.query(models.Exercise).filter(
        models.Exercise.muscle_group == target_exercise.muscle_group,
        models.Exercise.id != target_exercise.id
    ).limit(limit).all()
    return similar

def find_similar_foods_by_macros(db: Session, target_food: models.Food, tolerance: float = 0.1, limit: int = 5) -> List[Tuple[models.Food, float]]:
    """
    Find foods with similar macros (protein, carbs, fat per 100g) within a tolerance percentage
    Returns list of (food, similarity_score) where lower score is more similar
    """
    target_macros = (target_food.protein_per_100g, target_food.carbs_per_100g, target_food.fat_per_100g)
    
    # Get all foods except the target
    all_foods = db.query(models.Food).filter(models.Food.id != target_food.id).all()
    
    similar_foods = []
    for food in all_foods:
        food_macros = (food.protein_per_100g, food.carbs_per_100g, food.fat_per_100g)
        # Calculate Euclidean distance normalized by target values
        # Avoid division by zero
        diff_p = abs(food_macros[0] - target_macros[0]) / (target_macros[0] if target_macros[0] > 0 else 1)
        diff_c = abs(food_macros[1] - target_macros[1]) / (target_macros[1] if target_macros[1] > 0 else 1)
        diff_f = abs(food_macros[2] - target_macros[2]) / (target_macros[2] if target_macros[2] > 0 else 1)
        
        distance = (diff_p**2 + diff_c**2 + diff_f**2)**0.5
        
        # Only include if within tolerance
        if distance <= tolerance:
            similar_foods.append((food, distance))
    
    # Sort by distance (closest first)
    similar_foods.sort(key=lambda x: x[1])
    return similar_foods[:limit]
