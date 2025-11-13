from typing import List
from sqlalchemy.orm import Session

from core.pianos.piano_types import PianoType


class PianoTypeRepository:
    def __init__(self, session: Session):
        self.session_internal = session

    def get_by_id(self, piano_type_id: int) -> PianoType:
        return self.session_internal.query(PianoType).filter_by(id=piano_type_id).first()

    def get_by_name(self, piano_type_name: str) -> PianoType:
        return self.session_internal.query(PianoType).filter_by(name=piano_type_name).first()

    def get_all(self) -> List[PianoType]:
        return self.session_internal.query(PianoType).all()

    def add(self, piano_type: PianoType) -> PianoType:
        piano_type_from_db = self.get_by_name(piano_type.name)
        if not piano_type_from_db:
            self.session_internal.add(piano_type)
            self.session_internal.commit()
            return piano_type
        else:
            return None

    def update(self, piano_type: PianoType) -> PianoType:
        piano_type_from_db = self.get_by_id(piano_type.id)
        if piano_type_from_db:
            piano_type_from_db = piano_type
            self.session_internal.commit()
            return piano_type
        else:
            return None

    def delete(self, piano_type_id: int):
        piano_type_from_db = self.get_by_id(piano_type_id)
        if piano_type_from_db:
            self.session_internal.delete(piano_type_from_db)
            self.session_internal.commit()


