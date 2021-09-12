import os

from dependency_injector import containers, providers

from src.Services import UserService
from src.Repository import UserRespository, Database

def get_database_url():
    mysql_user = os.getenv("MYSQL_USER")
    mysql_pwd = os.getenv("MYSQL_PASSWORD")
    mysql_host = os.getenv("MYSQL_HOST")
    mysql_port = os.getenv("MYSQL_PORT")
    mysql_database = os.getenv("MYSQL_DATABASE")

    return f"mysql://{mysql_user}:{mysql_pwd}@{mysql_host}:{mysql_port}/{mysql_database}"


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    print(f"Conneting to {get_database_url()}")
    db = providers.Factory(Database.Database, db_url=get_database_url())

    user_repository = providers.Factory(
        UserRespository.UserRepository,
        session_factory=db.provided.session
    )

    user_service = providers.Factory(
        UserService.UserService,
        user_repository=user_repository
    )