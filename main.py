from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session, select
from dotenv import load_dotenv
from .models.product import Product, ProductInfo, ProductResponse
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

@app.post("/api/product", response_model=dict, tags=["CREATE"])
async def create_product(new_product: ProductInfo, db:Session = Depends(get_db)):
    insert_product = Product.model_validate(new_product)
    db.add(insert_product)
    db.commit()
    return {"msg":"Inserció correcta"}

@app.get("/api/product/{id}", response_model=ProductResponse, tags=["READ by ID"])
async def get_product_id(id: int, db: Session = Depends(get_db)):
    product_by_id=select(Product).where(Product.id == id)
    result= db.exec(product_by_id).first()
    return ProductResponse.model_validate(result)

@app.get("/api/product", response_model=ProductResponse, tags=["READ ALL"])
async def get_all_products(db: Session = Depends(get_db)):
    #Sensible data: supplier_email and supplier_phone
    all_products = db.exec(select(Product)).all()
    return [ProductResponse.model_validate(product) for product in all_products]

@app.get("/api/product/{name}", response_model=ProductResponse, tags=["READ by NAME"])
async def get_products_by_name(name: str, db: Session = Depends(get_db)):
    products_by_name = select(Product).where(Product.name == name)
    products_list = db.exec(products_by_name).all()
    return [ProductResponse.model_validate(product) for product in products_list]

@app.delete("/api/product/{id}", response_model=dict, tags=["DELETE"])
async def delete_product(id: int, db: Session = Depends(get_db)):
    query = select(Product).where(Product.id == id)
    delete_product = db.exec(query).first()
    db.delete(delete_product)
    db.commit()
    return {"msg":"l’eliminació ha sigut exitosa"}

@app.get("/api/product/{id}/partial", response_model=ProductPartial, tags=["READ PARTIALLY"])
async def get_product_partially(id: int, db: Session = Depends(get_db)):
    query = select()
    return