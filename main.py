from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session, select
from dotenv import load_dotenv
from .models.product import Product, ProductInfo, ProductResponse, ProductPartial, ProductOne, ProductTwo
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
    query=select(Product).where(Product.id == id)
    result= db.exec(query).first()
    return ProductResponse.model_validate(result)

@app.get("/api/product", response_model=list[ProductResponse], tags=["READ ALL"])
async def get_all_products(db: Session = Depends(get_db)):
    #Sensible data: supplier_email and supplier_phone
    query = select(Product)
    all_products = db.exec(query).all()
    return [ProductResponse.model_validate(product) for product in all_products]

@app.get("/api/product/name/{name}", response_model=list[ProductResponse], tags=["READ by NAME"])
async def get_products_by_name(name: str, db: Session = Depends(get_db)):
    query = select(Product).where(Product.name == name)
    products_list = db.exec(query).all()
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
    # Sensible data: supplier_email and supplier_phone
    query = select(Product).where(Product.id == id)
    result = db.exec(query).first()
    return ProductPartial.model_validate(result)

@app.put("/api/product/{id}", response_model=dict, tags=["UPDATE PRODUCT"])
async def total_update(id: int, product: ProductInfo, db: Session = Depends(get_db)):
    query = select(Product).where(Product.id == id)
    update_product = db.exec(query).first()
    changes = product
    update_product.sqlmodel_update(changes)
    db.add(update_product)
    db.commit()
    return {"msg":"Producte actualitzat"}

@app.patch("/api/product/{id}/price", response_model=dict, tags=["UPDATE one VALUE"])
async def update_one(id:int, product: ProductOne, db: Session = Depends(get_db)):
    query = select(Product).where(Product.id == id)
    update_product = db.exec(query).first()
    one_change = product
    update_product.price = one_change.price
    db.add(update_product)
    db.commit()
    return {"msg":"Preu actualitzat"}

@app.patch("/api/product/{id}/price-stock", response_model=dict, tags=["UPDATE two VALUE"])
async def update_one(id:int, product: ProductTwo, db: Session = Depends(get_db)):
    query = select(Product).where(Product.id == id)
    update_product= db.exec(query).first()
    two_changes = product
    update_product.price = two_changes.price
    update_product.stock = two_changes.stock
    db.add(update_product)
    db.commit()
    return {"msg":"Preu i estoc actualitzats"}
