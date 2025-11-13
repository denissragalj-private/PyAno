from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from infrastructure.database.database import Base
from config import NAME_LENGHT


class PianoType(Base):
    __tablename__ = 'piano_type'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(NAME_LENGHT), nullable=False)

    pianos = relationship('Piano', back_populates='piano_type')

    def __repr__(self):
        return f'Piano type: {self.name}'
