from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

DATABASE_URL = "sqlite:///./test.db"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a declarative base
Base = declarative_base()


# Create the session class
class Database:
    def __init__(self):
        self._engine = engine
        self._session_factory = orm.sessionmaker(bind=engine)

    def create_session(self) -> Session:
        return self._session_factory()

    def init_db(self):
        Base.metadata.create_all(bind=self._engine)


# Create an instance of the Database class
database = Database()