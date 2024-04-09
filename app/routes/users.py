from fastapi import APIRouter, HTTPException
from app.models import User
from app.services.user_service import UserService

router = APIRouter()
user_service = UserService()


@router.post("/", response_model=User)
def create_user(user: User):
    return user_service.create_user(user)


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    user = user_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
