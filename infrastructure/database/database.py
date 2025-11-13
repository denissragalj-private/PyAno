from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import DATABASE_PATH


engine = create_engine(DATABASE_PATH)

# koristiti čemo u MODEL klasama
Base = declarative_base()

# koristiti čemo u REPO klasama
Session = sessionmaker(bind=engine)

# session = Session() 
