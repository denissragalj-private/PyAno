from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship 

from infrastructure.database.database import Base 

from config import NAME_LENGTH




class Piano:
    __tablename__ = 'pianos'

    id = Column(Integer)
    name = Column(String(NAME_LENGTH))

    piano_category_id = Column(Integer)

    piano_category_id = relationship("PianoCategories", back_populates="pianos")    