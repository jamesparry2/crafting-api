from src.Services.UserService import UserService


class LoginService():
    def __init__(self, user_service: UserService, pwd) -> None:
        print(pwd)
        self._user_service = user_service

    def get_user_with_id(self, id: str):
        return self._user_service.get_by_id(id)