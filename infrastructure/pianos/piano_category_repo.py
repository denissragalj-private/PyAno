from typing import List
from sqlalchemy.orm import Session

from core.pianos.piano_categories import PianoCategory


class PianoCategoryRepository:
    def __init__(self, session: Session):
        self.session_internal = session

    def get_by_id(self, piano_category_id: int) -> PianoCategory:
        return self.session_internal.query(PianoCategory).filter_by(id = piano_category_id).first()

    def get_by_name(self, piano_category_name: str) -> PianoCategory:
        return self.session_internal.query(PianoCategory).filter_by(name = piano_category_name).first()

    def get_all(self) -> List[PianoCategory]:
        return self.session_internal.query(PianoCategory).all()

    def add(self, piano_category: PianoCategory) -> PianoCategory | None:
        piano_category_from_db = self.get_by_name(piano_category.name)
        if piano_category_from_db == None:
            self.session_internal.add(piano_category)
            self.session_internal.commit()
            return piano_category
        else:
            return None

    def update(self, piano_category: PianoCategory) -> PianoCategory:
        piano_category_from_db = self.get_by_id(piano_category.id)
        if piano_category_from_db != None:
            piano_category_from_db = piano_category
            self.session_internal.commit()
            return piano_category_from_db
        else:
            return None

    def delete(self, piano_category_id: int):
        piano_category_from_db = self.get_by_id(piano_category_id)
        if piano_category_from_db != None:
            self.session_internal.delete(piano_category_from_db)
            self.session_internal.commit()
        else:
            return None
