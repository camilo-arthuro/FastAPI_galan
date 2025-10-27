from sqlmodel import SQLModel, Field

class Product(SQLModel, table = True):
    id: int = Field(default=None, primary_key=True)
    name: str
    price: float
    stock: int
    supplier_email: str
    supplier_phone: str

class ProductInfo(SQLModel):
    name: str
    price: float
    stock: int
    supplier_email: str
    supplier_phone: str

class ProductResponse(SQLModel):
    id: int
    name: str
    price: float
    stock: int

class ProductPartial(SQLModel):
    name: str
    price: float
    stock: int

class ProductOne(SQLModel):
    price: float

class ProductTwo(SQLModel):
    price: float
    stock: int
