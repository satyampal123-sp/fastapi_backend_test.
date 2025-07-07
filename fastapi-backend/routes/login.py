from fastapi import APIRouter
from models import LoginRequest, LoginResponse
from auth import authenticate_user

router = APIRouter()

@router.post("/login/", response_model=LoginResponse)
def login(data: LoginRequest):
    token = authenticate_user(data.username, data.password)
    return {"token": token}
