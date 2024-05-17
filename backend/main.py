from factory import create_app
from db.session import engine
from db.base import Base


def create_tables():
    Base.metadata.create_all(bind=engine)
    
    
def start_application():
    app = create_app()
    create_tables()
    return app


app = start_application()
