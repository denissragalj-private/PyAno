from sqlalchemy import Column, Integer, String

from infrastructure.database.database import Base
from config import NAME_LENGHT, DESCRIPTION_LENGHT, URL_LENGHT


class PianoChords(Base):
    __tablename__ = 'piano_chords'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(NAME_LENGHT), nullable=False)

    description = Column(String(DESCRIPTION_LENGHT), nullable=True)
    image_url = Column(String(URL_LENGHT), nullable=True)

    def __repr__(self):
        if self.id:
            return f'Piano chord: ({self.id}) {self.name}'
        else:
            return f'Piano chord: {self.name}'
