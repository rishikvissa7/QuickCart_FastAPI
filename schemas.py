from pydantic import BaseModel
from typing import Optional, List


class UserCreate(BaseModel):
    username: str
    password: str
    role: str = "user"

class UserShow(BaseModel):
    id: int
    username: str
    role: str

class Token(BaseModel):
    access_token: str
    token_type: str

class Credentials(BaseModel):
    username: str
    password: str

class ProductCreate(BaseModel):
    name: str
    description: Optional[str]
    price: float
    stock: int
    category_id: int

class ProductShow(ProductCreate):
    id: int

class CategoryCreate(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryShow(CategoryCreate):
    id: int
