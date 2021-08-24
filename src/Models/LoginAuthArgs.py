from pydantic import BaseModel

class LoginAuthArgs(BaseModel):
    username: str
    password: str