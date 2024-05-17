from fastapi.testclient import TestClient
import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from factory import create_app
from db.base import Base
from db.session import get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def app():
    Base.metadata.create_all(bind=engine)
    _app = create_app()
    yield _app
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def db_session():
    connection = engine.connect()
    transaction = connection.begin()
    session = SessionTesting(bind=connection)
    yield session
    session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture(scope="function")
def client(app, db_session):
    def _get_test_db():
        try:
            yield db_session
        finally:
            pass
        
    app.dependency_overrides[get_db] = _get_test_db
    
    with TestClient(app) as client:
        yield client