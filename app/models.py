from pydantic import BaseModel
from typing import List, Optional


class User(BaseModel):
    id: int
    name: str
    email: str
    payment_methods: List[int] = []


class PaymentMethod(BaseModel):
    id: int
    name: Optional[str]
    logo_url: Optional[str]
    short_name: str
    description: str
