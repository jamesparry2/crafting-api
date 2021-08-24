from src.Repository.UserRespository import User, UserRepository


class UserService():
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

    def get_by_id(self, id: str) -> User:
        return self._user_repository.get_user(id)