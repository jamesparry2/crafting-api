from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from src.Container import Container
from src.Models.LoginAuthArgs import LoginAuthArgs
from src.Services.LoginService import LoginService

router = APIRouter(prefix="/login", tags=["login"])
        
@router.get("/authenticate")
@inject
def authenticate_user(
    login_params: LoginAuthArgs = Depends(),
    login_service: LoginService = Depends(Provide[Container.login_service]),
):
    response = login_service.get_user_with_id("ID_TEST")
    return response