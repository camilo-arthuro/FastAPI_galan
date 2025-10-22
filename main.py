from fastapi import FastAPI, Depends
#from pydantic import BaseModel
from sqlmodel import SQLModel, create_engine, Session, select
from dotenv import load_dotenv
from models.product import Product, ProductInfo, ProductResponse
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

@app.post("/api/users", response_model=dict, tags=["CREATE"])
async def create_product(new_product: ProductInfo, db:Session = Depends(get_db)):
    insert_product = Product.model_validate(new_product)
    db.add(insert_product)
    db.commit()
    return {"msg":"Inserció correcta"}

@app.get("/api/users/{id}", response_model=ProductResponse, tags=["READ by ID"])
async def get_user_id(id: int, db: Session = Depends(get_db)):
    product_by_id=select(Product).where(Product.id == id)
    result= db.exec(product_by_id).first()
    return ProductResponse.model_validate(result)
'''
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
'''