from sqlmodel import SQLModel, Field

class Product(SQLModel, table = True):
    id: int = Field(default=None, primary_key=True)
    name: str
    description: str
    price: float
    stock: int
    supplier_email: str

class ProductInfo(SQLModel):
    name: str
    description: str
    price: float
    stock: int
    supplier_email: str

class ProductResponse(SQLModel):
    id: int
    name: str
    description: str
    price: float
    stock: int