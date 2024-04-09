from typing import List

from fastapi import APIRouter

from app.models import PaymentMethod
from app.services.payment_method_service import PaymentMethodService

router = APIRouter()

payment_method_service = PaymentMethodService()


@router.get("/", response_model=List[PaymentMethod])
def get_payment_methods(user_id: int = None, status: str = None, type: str = None):
    return payment_method_service.get_payment_methods(user_id, status, type)


@router.post("/", response_model=PaymentMethod)
def create_payment_method(payment_method: PaymentMethod):
    return payment_method_service.create_payment_method(payment_method)


@router.put("/{payment_method_id}", response_model=PaymentMethod)
def update_payment_method(payment_method_id: int, payment_method: PaymentMethod):
    return payment_method_service.update_payment_method(payment_method_id, payment_method)


@router.delete("/{payment_method_id}")
def delete_payment_method(payment_method_id: int):
    payment_method_service.delete_payment_method(payment_method_id)
    return {"message": "Payment method deleted"}
