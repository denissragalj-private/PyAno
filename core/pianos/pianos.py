from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship

from infrastructure.database.database import Base
from config import NAME_LENGHT, DESCRIPTION_LENGHT, URL_LENGHT, LOCATION_STR


class Piano(Base):
    __tablename__ = 'piano'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(NAME_LENGHT), nullable=False)
    price = Column(DECIMAL(scale=18, precision=6), nullable=False, default=0.0)

    description = Column(String(DESCRIPTION_LENGHT), nullable=True)
    image_url = Column(String(URL_LENGHT), nullable=True)
    location = Column(String(LOCATION_STR), nullable=True)

    piano_type = relationship('PianoType', back_populates='pianos')
    piano_type_id = Column(Integer, ForeignKey('piano_type.id'))

    piano_category = relationship('PianoCategory', back_populates='pianos')
    piano_category_id = Column(Integer, ForeignKey('piano_category.id'))


    def __repo
