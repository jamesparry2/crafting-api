from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from src.Container import Container
from src.Services.UserService import UserService
from src.Models.Request.UserRegisterRequest import UserRegisterRequest

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register")
@inject
def register_user(
    user_params: UserRegisterRequest,
    user_service: UserService = Depends(Provide[Container.user_service])
):
    return user_service.add_user(user_params)