from src.Models.Request.UserRegisterRequest import UserRegisterRequest
from src.Repository.UserRespository import User, UserRepository


class UserService():
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    def get_by_id(self, id: str) -> User:
        return self._user_repository.get_user(id)

    def add_user(self, user: UserRegisterRequest) -> bool:
        return self._user_repository.create_user(user)

    def login_user(self, user_request: UserRegisterRequest) -> str:
        user = self._user_repository.get_user_by_username(user_request.username)
        if user is None:
            return "Username provided does not exist"
        
        if not user.is_password_hashed_equivalent(user_request.password):
            return "Password provided is invalid"
        
        return "This will be a JWT Token"