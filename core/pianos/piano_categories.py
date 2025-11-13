from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from infrastructure.database.database import Base
from config import NAME_LENGHT


class PianoCategory(Base):
    __tablename__ = 'piano_category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(NAME_LENGHT), nullable=False)

    pianos = relationship('Piano', back_populates='piano_category')




    # ACOUSTIC = "acoustic"
    # ELECTRIC = "electric"
    # GRAND = "grand"
    # UPRIGHT = "upright"
    # DIGITAL = "digital"
    # HYBRID = "hybrid"
