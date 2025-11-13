from core.pianos.piano_categories import PianoCategory
from core.pianos.piano_types import PianoType
from .database.database import Base, engine, get_sesion
from infrastructure.pianos.piano_repo import PianoRepository
from infrastructure.pianos.piano_category_repo import PianoCategoryRepository
from infrastructure.pianos.piano_type_repo import PianoTypeRepository
from infrastructure.chords.piano_chords_repo import PianoChordRepository
from config import PIANO_CATEGORIES, PIANO_TYPES


class BaseRepository:
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = get_sesion()

        self.piano_repo = PianoRepository(self.session)
        self.piano_category_repo = PianoCategoryRepository(self.session)
        self.piano_type_repo = PianoTypeRepository(self.session)

        self.piano_chord_repo = PianoChordRepository(self.session)

    def db_seed(self):
        for piano_category in PIANO_CATEGORIES:
            self.piano_category_repo.add(PianoCategory(name=piano_category))

        for piano_type in PIANO_TYPES:
            self.piano_type_repo.add(PianoType(name=piano_type))
