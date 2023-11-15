from fastapi import FastAPI, HTTPException
from uuid import UUID
from typing import List
from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("7150e816-8654-46ca-91ec-7a423b08ed1f"), 
        first_name="Isti",
        middle_name="Hana",
        last_name="Fatimah",
        gender=Gender.female,
        roles=[Role.student]
    ),
    User(
        id=UUID("9a947794-17c1-4600-804e-3b9831102a5f"), 
        first_name="Rosyad",
        middle_name="Ghani",
        last_name="Alkhawarizmi",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

# GET ALL USER
@app.get("/api/v1/users")
async def fetch_users():
    return {"data":db}

# ADD NEW USER
@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {
        "message":"Data has been added!",
        "id": user.id
    }

# DELETE USER
@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {
                "message": "Data has been deleted!",
                "id":user.id
            }
    raise HTTPException(
        status_code=404,
        detail=f"Data with id: {user_id} does not exists"
    )

