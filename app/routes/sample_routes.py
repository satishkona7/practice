from fastapi import APIRouter
from app.services.sample_service import get_message, get_secret_message

router = APIRouter(prefix="/api", tags=["Sample"])


@router.get("/hello")
def say_hello():
    message = get_message()
    return {"message": message}


@router.get("/secret")
def get_secret():
    message = get_secret_message()
    return {"secret": message}