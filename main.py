from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)

def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

users_list = []

@app.post("/api/users", response_model=dict)
async def create_user(new_user: str):
    users_list.append(new_user)
    numbers = range(len(users_list))
    users_dic = dict(zip(numbers, users_list))
    return users_dic

@app.get("/api/users/{id}", response_model=dict)
async def get_user_id(id: int):
    users_dic = {}
    users_dic[id]=users_list[id]
    return users_dic

@app.get("/api/users", response_model=dict)
async def get_all_users():
    numbers = range(len(users_list))
    users_dic = dict(zip(numbers, users_list))
    return users_dic

@app.put("/api/users/{id}", response_model=dict)
async def update_user(id: int, updated_user: str):
    users_dic = {}
    users_list[id] = updated_user
    users_dic[id] = users_list[id]
    return users_dic

@app.delete("/api/usuaris/{id}", response_model=dict)
async def delete_user(id: int):
    users_list.pop(id)
    numbers = range(len(users_list))
    users_dic = dict(zip(numbers, users_list))
    return users_dic