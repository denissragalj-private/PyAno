from typing import List
from sqlalchemy.orm import Session

from core.pianos.pianos import Piano


class PianoRepository:
    def __init__(self, session: Session):
        self.session_internal = session

    def get_by_id(self, piano_id: int) -> Piano:
        return self.session_internal.query(Piano).filter_by(id=piano_id).first()

    def get_by_name(self, piano_name: str) -> Piano:
        return self.session_internal.query(Piano).filter_by(name=piano_name).first()

    def get_all(self) -> List[Piano]:
        return self.session_internal.query(Piano).all()

    def add(self, piano: Piano) -> Piano:
        piano_from_db = self.get_by_name(piano.name)
        if not piano_from_db:
            self.session_internal.add(piano)
            self.session_internal.commit()
            return piano
        else:
            return None

    def update(self, piano: Piano) -> Piano:
        piano_from_db = self.get_by_id(piano.id)
        if piano_from_db:
            piano_from_db = piano
            self.session_internal.commit()
            return piano_from_db
        else:
            return None

    def delete(self, piano_id: int):
        piano_from_db = self.get_by_id(piano_id)
        if piano_from_db:
            self.session_internal.delete(piano_from_db)
            self.session_internal.commit()
