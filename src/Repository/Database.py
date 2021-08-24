from contextlib import contextmanager
from typing import Callable

from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

Base = declarative_base()

class Database:
    def __init__(self, db_url) -> None:
        print("Database" + db_url)
        self._engine = create_engine(url=db_url, echo=True)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )
    
    @contextmanager
    def session(self) -> Session:
        session: Session = self._session_factory()
        try:
            yield session
        except:
            session.rollback()
            raise
        finally:
            session.close()