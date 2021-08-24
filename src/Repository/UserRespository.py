import hashlib
from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy.orm import Session
from sqlalchemy import Column, String, Integer

from src.Utils.hashing import hash_password_with_salt
from src.Repository.Database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    hashed_password = Column(String)

    def __repr__(self) -> str:
        return f'<User(id="{self.id}", ' \
               f'user_name="{self.user_name}", ' \
               f'hashed_password="{self.hashed_password}")>'

class UserRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_user(self, id: str) -> User:
        with self.session_factory() as db_session:
            response: User = db_session.query(User).filter(User.id == 1).first()
            print(response)
            return response
