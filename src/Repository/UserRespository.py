import hashlib
from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy.orm import Session
from sqlalchemy import Column, String, Integer
import bcrypt

from src.Models.Request.UserRegisterRequest import UserRegisterRequest
from src.Repository.Database import Base

encode_type = "utf-8"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    hashed_password = Column(String)

    def is_password_hashed_equivalent(self, inbound_password: str) -> bool:
        return bcrypt.checkpw(inbound_password.encode(encode_type), self.hashed_password)
    
    def set_password(self, password: str) -> None:
        self.hashed_password = bcrypt.hashpw(password.encode(encode_type), bcrypt.gensalt(10))

    def __repr__(self) -> str:
        return f'<User(id="{self.id}", ' \
               f'user_name="{self.user_name}", ' \
               f'hashed_password="{self.hashed_password}")>'

class UserRepository:
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]) -> None:
        self.session_factory = session_factory

    def get_user_by_username(self, user_name: str) -> User:
        with self.session_factory() as db_session:
            response: User = db_session.query(User).filter(User.user_name == user_name).first()
            return response

    def create_user(self, user_request: UserRegisterRequest) -> bool:
        with self.session_factory() as db_session:
            try:
                user = User(user_name=user_request.username)
                user.set_password(user_request.password)
                db_session.add(user)
                db_session.commit()
                return True
            except Exception as error:
                print(error)
                return False