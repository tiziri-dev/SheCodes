import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine_test = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)


@pytest.fixture(scope="function")
def db():
    """Base de données en mémoire pour les tests."""
    try:
        from app.database import Base
        Base.metadata.create_all(bind=engine_test)
    except ImportError:
        pass

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        try:
            from app.database import Base
            Base.metadata.drop_all(bind=engine_test)
        except ImportError:
            pass


@pytest.fixture(scope="function")
def client(db):
    """Client de test FastAPI."""
    try:
        from app.main import app
        from app.database import get_db

        def override_get_db():
            try:
                yield db
            finally:
                db.close()

        app.dependency_overrides[get_db] = override_get_db
        with TestClient(app) as c:
            yield c
        app.dependency_overrides.clear()
    except ImportError:
        pytest.skip("app.main pas encore disponible")
