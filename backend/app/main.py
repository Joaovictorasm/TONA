
from fastapi import FastAPI
from app.routers import protocols, exercises, foods

app = FastAPI(title="FitNut Platform", version="0.1.0")

app.include_router(protocols.router, prefix="/protocols", tags=["protocols"])
app.include_router(exercises.router, prefix="/exercises", tags=["exercises"])
app.include_router(foods.router, prefix="/foods", tags=["foods"])

@app.get("/")
async def root():
    return {"message": "Welcome to FitNut Platform API"}
