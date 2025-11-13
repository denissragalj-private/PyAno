from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

from config import DATABASE_PATH


engine = create_engine(DATABASE_PATH)

# Koristiti cemo u MODEL klasama
Base = declarative_base()

# Koristiti cemo u REPO klasama
def get_sesion() -> Session:
    return Session(bind=engine)
