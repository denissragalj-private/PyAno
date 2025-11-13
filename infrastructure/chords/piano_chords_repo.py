from typing import List
from sqlalchemy.orm import Session

from core.chords.piano_chords import PianoChords


class PianoChordRepository:
    def __init__(self, session: Session):
        self.session_internal = session

    def get_by_id(self, piano_chord_id: int) -> PianoChords:
        return self.session_internal.query(PianoChords).filter_by(id=piano_chord_id).first()

    def get_by_name(self, piano_chord_name: str) -> PianoChords:
        return self.session_internal.query(PianoChords).filter_by(name=piano_chord_name).first()

    def get_all(self) -> List[PianoChords]:
        return self.session_internal.query(PianoChords).all()

    def add(self, piano_chord: PianoChords) -> PianoChords:
        piano_chord_from_db = self.get_by_name(piano_chord.name)
        if not piano_chord_from_db:
            self.session_internal.add(piano_chord)
            self.session_internal.commit()
            return piano_chord
        else:
            return None

    def update(self, piano_chord: PianoChords) -> PianoChords:
        piano_chord_from_db = self.get_by_id(piano_chord.id)
        if piano_chord_from_db:
            piano_chord_from_db = piano_chord
            self.session_internal.commit()
            return piano_chord_from_db
        else:
            return None

    def delete(self, piano_chord_id: int):
        piano_chord_from_db = self.get_by_id(piano_chord_id)
        if piano_chord_from_db:
            self.session_internal.delete(piano_chord_from_db)
            self.session_internal.commit()
