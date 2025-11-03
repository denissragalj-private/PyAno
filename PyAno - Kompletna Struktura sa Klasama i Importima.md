<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# PyAno - Kompletna Struktura sa Klasama i Importima

```bash
PyAno
|   .gitattributes
|   .gitignore
|   app.py
|   config.py
|   config.yaml
|   README.md
|   tree.txt
|   
+---core
|   |   __init__.py
|   |   
|   +---chords
|   |       chord.py
|   |       __init__.py
|   |       
|   +---circles
|   |       circle.py
|   |       __init__.py
|   |       
|   +---lessons
|   |       lesson.py
|   |       __init__.py
|   |       
|   +---pianos
|   |       piano.py
|   |       piano_category.py
|   |       piano_type.py
|   |       __init__.py
|   |       
|   +---scales
|   |       scale.py
|   |       __init__.py
|   |       
|   \---tones
|           tone.py
|           __init__.py
|           
+---data_store
|   +---db
|   |       py_ano.db
|   |       
|   \---files
|           chords.json
|           circles.json
|           lessons.json
|           pianos.json
|           scales.json
|           tones.json
|           
+---gui
|   |   main_menu.py
|   |   __init__.py
|   |   
|   \---menu_items
|       |   lessons_menu_items.py
|       |   pianos_menu_items.py
|       |   __init__.py
|       |       
|       \---music_theory
|               chords_menu_items.py
|               circles_menu_items.py
|               music_theory_menu_items.py
|               scales_menu_items.py
|               tones_menu_items.py
|               __init__.py
|               
+---infrastructure
|   |   base_repository.py
|   |   __init__.py
|   |   
|   +---chords
|   |       chord_repository.py
|   |       __init__.py
|   |       
|   +---circles
|   |       circle_repository.py
|   |       __init__.py
|   |       
|   +---lessons
|   |       lesson_repository.py
|   |       __init__.py
|   |       
|   +---pianos
|   |       piano_repository.py
|   |       __init__.py
|   |       
|   +---scales
|   |       scale_repository.py
|   |       __init__.py
|   |       
|   \---tones
|           tone_repository.py
|           __init__.py
|           
+---services
|   |   __init__.py
|   |   
|   +---chords
|   |       chord_service.py
|   |       __init__.py
|   |       
|   +---circles
|   |       circle_service.py
|   |       __init__.py
|   |       
|   +---lessons
|   |       lesson_service.py
|   |       __init__.py
|   |       
|   +---pianos
|   |       piano_service.py
|   |       __init__.py
|   |       
|   +---scales
|   |       scale_service.py
|   |       __init__.py
|   |       
|   \---tones
|           tone_service.py
|           __init__.py
|           
\---venv
```


## Sadržaj Svih Datoteka

### CORE PAKET - Modeli

#### `core/__init__.py`

```python
from core.pianos.piano import Piano
from core.pianos.piano_category import PianoCategory
from core.pianos.piano_type import PianoType
from core.tones.tone import Tone
from core.scales.scale import Scale
from core.chords.chord import Chord
from core.circles.circle import Circle
from core.lessons.lesson import Lesson

__all__ = [
    'Piano',
    'PianoCategory',
    'PianoType',
    'Tone',
    'Scale',
    'Chord',
    'Circle',
    'Lesson'
]
```


#### `core/pianos/piano.py`

```python
from datetime import datetime

class Piano:
    def __init__(self, id, name, category, piano_type, manufacturer, price, year,
                 description=None, deleted=False, deleted_at=None, 
                 created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.category = category
        self.piano_type = piano_type
        self.manufacturer = manufacturer
        self.price = price
        self.year = year
        self.description = description
        self.deleted = deleted
        self.deleted_at = deleted_at
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()
    
    def to_dict(self):
        pass
    
    def __str__(self):
        pass
```


#### `core/pianos/piano_category.py`

```python
from datetime import datetime

class PianoCategory:
    def __init__(self, id, name, description=None, deleted=False, 
                 deleted_at=None, created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.description = description
        self.deleted = deleted
        self.deleted_at = deleted_at
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()
    
    def to_dict(self):
        pass
    
    def __str__(self):
        pass
```


#### `core/pianos/piano_type.py`

```python
from datetime import datetime

class PianoType:
    def __init__(self, id, name, description=None, deleted=False, 
                 deleted_at=None, created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.description = description
        self.deleted = deleted
        self.deleted_at = deleted_at
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()
    
    def to_dict(self):
        pass
    
    def __str__(self):
        pass
```


#### `core/pianos/__init__.py`

```python
from core.pianos.piano import Piano
from core.pianos.piano_category import PianoCategory
from core.pianos.piano_type import PianoType

__all__ = ['Piano', 'PianoCategory', 'PianoType']
```


#### `core/tones/tone.py`

```python
from datetime import datetime

class Tone:
    def __init__(self, id, name, frequency, octave, notation=None,
                 deleted=False, deleted_at=None, created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.frequency = frequency
        self.octave = octave
        self.notation = notation
        self.deleted = deleted
        self.deleted_at = deleted_at
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()
    
    def to_dict(self):
        pass
    
    def __str__(self):
        pass
```


#### `core/tones/__init__.py`

```python
from core.tones.tone import Tone

__all__ = ['Tone']
```


#### `core/scales/scale.py`

```python
from datetime import datetime

class Scale:
    def __init__(self, id, name, notes, scale_type, description=None,
                 deleted=False, deleted_at=None, created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.notes = notes
        self.scale_type = scale_type
        self.description = description
        self.deleted = deleted
        self.deleted_at = deleted_at
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()
    
    def to_dict(self):
        pass
    
    def __str__(self):
        pass
```


#### `core/scales/__init__.py`

```python
from core.scales.scale import Scale

__all__ = ['Scale']
```


#### `core/chords/chord.py`

```python
from datetime import datetime

class Chord:
    def __init__(self, id, name, notes, chord_type, intervals=None, description=None,
                 deleted=False, deleted_at=None, created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.notes = notes
        self.chord_type = chord_type
        self.intervals = intervals
        self.description = description
        self.deleted = deleted
        self.deleted_at = deleted_at
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()
    
    def to_dict(self):
        pass
    
    def __str__(self):
        pass
```


#### `core/chords/__init__.py`

```python
from core.chords.chord import Chord

__all__ = ['Chord']
```


#### `core/circles/circle.py`

```python
from datetime import datetime

class Circle:
    def __init__(self, id, name, circle_type, keys, description=None,
                 deleted=False, deleted_at=None, created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.circle_type = circle_type
        self.keys = keys
        self.description = description
        self.deleted = deleted
        self.deleted_at = deleted_at
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()
    
    def to_dict(self):
        pass
    
    def __str__(self):
        pass
```


#### `core/circles/__init__.py`

```python
from core.circles.circle import Circle

__all__ = ['Circle']
```


#### `core/lessons/lesson.py`

```python
from datetime import datetime

class Lesson:
    def __init__(self, id, title, content, difficulty_level, duration=None, 
                 category=None, deleted=False, deleted_at=None, 
                 created_at=None, updated_at=None):
        self.id = id
        self.title = title
        self.content = content
        self.difficulty_level = difficulty_level
        self.duration = duration
        self.category = category
        self.deleted = deleted
        self.deleted_at = deleted_at
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()
    
    def to_dict(self):
        pass
    
    def __str__(self):
        pass
```


#### `core/lessons/__init__.py`

```python
from core.lessons.lesson import Lesson

__all__ = ['Lesson']
```


***

### INFRASTRUCTURE PAKET - Repozitoriji

#### `infrastructure/__init__.py`

```python
from infrastructure.base_repository import BaseJsonRepository
from infrastructure.pianos.piano_repository import PianoRepository
from infrastructure.tones.tone_repository import ToneRepository
from infrastructure.scales.scale_repository import ScaleRepository
from infrastructure.chords.chord_repository import ChordRepository
from infrastructure.circles.circle_repository import CircleRepository
from infrastructure.lessons.lesson_repository import LessonRepository

__all__ = [
    'BaseJsonRepository',
    'PianoRepository',
    'ToneRepository',
    'ScaleRepository',
    'ChordRepository',
    'CircleRepository',
    'LessonRepository'
]
```


#### `infrastructure/base_repository.py`

```python
import json
import os
from datetime import datetime

class BaseJsonRepository:
    def __init__(self, file_path, model_class):
        self.file_path = file_path
        self.model_class = model_class
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        pass
    
    def _read_all(self):
        pass
    
    def _write_all(self, data):
        pass
    
    def _get_next_id(self, data):
        pass
    
    def create(self, entity):
        pass
    
    def get_by_id(self, entity_id):
        pass
    
    def get_all(self, include_deleted=False):
        pass
    
    def update(self, entity_id, update_dict):
        pass
    
    def soft_delete(self, entity_id):
        pass
    
    def _dict_to_entity(self, data_dict):
        pass
```


#### `infrastructure/pianos/piano_repository.py`

```python
from infrastructure.base_repository import BaseJsonRepository
from core.pianos.piano import Piano

class PianoRepository(BaseJsonRepository):
    def __init__(self, file_path):
        super().__init__(file_path, Piano)
    
    def get_by_category(self, category):
        pass
    
    def get_by_manufacturer(self, manufacturer):
        pass
    
    def get_by_price_range(self, min_price, max_price):
        pass
    
    def get_by_year_range(self, min_year, max_year):
        pass
```


#### `infrastructure/pianos/__init__.py`

```python
from infrastructure.pianos.piano_repository import PianoRepository

__all__ = ['PianoRepository']
```


#### `infrastructure/tones/tone_repository.py`

```python
from infrastructure.base_repository import BaseJsonRepository
from core.tones.tone import Tone

class ToneRepository(BaseJsonRepository):
    def __init__(self, file_path):
        super().__init__(file_path, Tone)
    
    def get_by_octave(self, octave):
        pass
    
    def get_by_frequency_range(self, min_freq, max_freq):
        pass
```


#### `infrastructure/tones/__init__.py`

```python
from infrastructure.tones.tone_repository import ToneRepository

__all__ = ['ToneRepository']
```


#### `infrastructure/scales/scale_repository.py`

```python
from infrastructure.base_repository import BaseJsonRepository
from core.scales.scale import Scale

class ScaleRepository(BaseJsonRepository):
    def __init__(self, file_path):
        super().__init__(file_path, Scale)
    
    def get_by_type(self, scale_type):
        pass
    
    def search_by_notes(self, notes):
        pass
```


#### `infrastructure/scales/__init__.py`

```python
from infrastructure.scales.scale_repository import ScaleRepository

__all__ = ['ScaleRepository']
```


#### `infrastructure/chords/chord_repository.py`

```python
from infrastructure.base_repository import BaseJsonRepository
from core.chords.chord import Chord

class ChordRepository(BaseJsonRepository):
    def __init__(self, file_path):
        super().__init__(file_path, Chord)
    
    def get_by_type(self, chord_type):
        pass
    
    def search_by_notes(self, notes):
        pass
```


#### `infrastructure/chords/__init__.py`

```python
from infrastructure.chords.chord_repository import ChordRepository

__all__ = ['ChordRepository']
```


#### `infrastructure/circles/circle_repository.py`

```python
from infrastructure.base_repository import BaseJsonRepository
from core.circles.circle import Circle

class CircleRepository(BaseJsonRepository):
    def __init__(self, file_path):
        super().__init__(file_path, Circle)
    
    def get_by_type(self, circle_type):
        pass
```


#### `infrastructure/circles/__init__.py`

```python
from infrastructure.circles.circle_repository import CircleRepository

__all__ = ['CircleRepository']
```


#### `infrastructure/lessons/lesson_repository.py`

```python
from infrastructure.base_repository import BaseJsonRepository
from core.lessons.lesson import Lesson

class LessonRepository(BaseJsonRepository):
    def __init__(self, file_path):
        super().__init__(file_path, Lesson)
    
    def get_by_difficulty(self, difficulty_level):
        pass
    
    def get_by_category(self, category):
        pass
```


#### `infrastructure/lessons/__init__.py`

```python
from infrastructure.lessons.lesson_repository import LessonRepository

__all__ = ['LessonRepository']
```


***

### SERVICES PAKET - Servisi

#### `services/__init__.py`

```python
from services.pianos.piano_service import PianoService
from services.tones.tone_service import ToneService
from services.scales.scale_service import ScaleService
from services.chords.chord_service import ChordService
from services.circles.circle_service import CircleService
from services.lessons.lesson_service import LessonService

__all__ = [
    'PianoService',
    'ToneService',
    'ScaleService',
    'ChordService',
    'CircleService',
    'LessonService'
]
```


#### `services/pianos/piano_service.py`

```python
from infrastructure.pianos.piano_repository import PianoRepository
from core.pianos.piano import Piano

class PianoService:
    def __init__(self, data_dir):
        self.repository = PianoRepository(f"{data_dir}/files/pianos.json")
    
    def create_piano(self, name, category, piano_type, manufacturer, price, year, description=None):
        pass
    
    def get_piano(self, piano_id):
        pass
    
    def list_all_pianos(self):
        pass
    
    def update_piano(self, piano_id, **kwargs):
        pass
    
    def delete_piano(self, piano_id):
        pass
    
    def search_by_category(self, category):
        pass
    
    def search_by_manufacturer(self, manufacturer):
        pass
    
    def search_by_price(self, min_price, max_price):
        pass
```


#### `services/pianos/__init__.py`

```python
from services.pianos.piano_service import PianoService

__all__ = ['PianoService']
```


#### `services/tones/tone_service.py`

```python
from infrastructure.tones.tone_repository import ToneRepository
from core.tones.tone import Tone

class ToneService:
    def __init__(self, data_dir):
        self.repository = ToneRepository(f"{data_dir}/files/tones.json")
    
    def create_tone(self, name, frequency, octave, notation=None):
        pass
    
    def get_tone(self, tone_id):
        pass
    
    def list_all_tones(self):
        pass
    
    def update_tone(self, tone_id, **kwargs):
        pass
    
    def delete_tone(self, tone_id):
        pass
    
    def get_by_octave(self, octave):
        pass
```


#### `services/tones/__init__.py`

```python
from services.tones.tone_service import ToneService

__all__ = ['ToneService']
```


#### `services/scales/scale_service.py`

```python
from infrastructure.scales.scale_repository import ScaleRepository
from core.scales.scale import Scale

class ScaleService:
    def __init__(self, data_dir):
        self.repository = ScaleRepository(f"{data_dir}/files/scales.json")
    
    def create_scale(self, name, notes, scale_type, description=None):
        pass
    
    def get_scale(self, scale_id):
        pass
    
    def list_all_scales(self):
        pass
    
    def update_scale(self, scale_id, **kwargs):
        pass
    
    def delete_scale(self, scale_id):
        pass
    
    def get_by_type(self, scale_type):
        pass
```


#### `services/scales/__init__.py`

```python
from services.scales.scale_service import ScaleService

__all__ = ['ScaleService']
```


#### `services/chords/chord_service.py`

```python
from infrastructure.chords.chord_repository import ChordRepository
from core.chords.chord import Chord

class ChordService:
    def __init__(self, data_dir):
        self.repository = ChordRepository(f"{data_dir}/files/chords.json")
    
    def create_chord(self, name, notes, chord_type, intervals=None, description=None):
        pass
    
    def get_chord(self, chord_id):
        pass
    
    def list_all_chords(self):
        pass
    
    def update_chord(self, chord_id, **kwargs):
        pass
    
    def delete_chord(self, chord_id):
        pass
    
    def get_by_type(self, chord_type):
        pass
```


#### `services/chords/__init__.py`

```python
from services.chords.chord_service import ChordService

__all__ = ['ChordService']
```


#### `services/circles/circle_service.py`

```python
from infrastructure.circles.circle_repository import CircleRepository
from core.circles.circle import Circle

class CircleService:
    def __init__(self, data_dir):
        self.repository = CircleRepository(f"{data_dir}/files/circles.json")
    
    def create_circle(self, name, circle_type, keys, description=None):
        pass
    
    def get_circle(self, circle_id):
        pass
    
    def list_all_circles(self):
        pass
    
    def update_circle(self, circle_id, **kwargs):
        pass
    
    def delete_circle(self, circle_id):
        pass
```


#### `services/circles/__init__.py`

```python
from services.circles.circle_service import CircleService

__all__ = ['CircleService']
```


#### `services/lessons/lesson_service.py`

```python
from infrastructure.lessons.lesson_repository import LessonRepository
from core.lessons.lesson import Lesson

class LessonService:
    def __init__(self, data_dir):
        self.repository = LessonRepository(f"{data_dir}/files/lessons.json")
    
    def create_lesson(self, title, content, difficulty_level, duration=None, category=None):
        pass
    
    def get_lesson(self, lesson_id):
        pass
    
    def list_all_lessons(self):
        pass
    
    def update_lesson(self, lesson_id, **kwargs):
        pass
    
    def delete_lesson(self, lesson_id):
        pass
    
    def get_by_difficulty(self, difficulty_level):
        pass
    
    def get_by_category(self, category):
        pass
```


#### `services/lessons/__init__.py`

```python
from services.lessons.lesson_service import LessonService

__all__ = ['LessonService']
```


***

### GUI PAKET - Korisnički Interfejs

#### `gui/__init__.py`

```python
from gui.main_menu import MainMenu

__all__ = ['MainMenu']
```


#### `gui/main_menu.py`

```python
from gui.menu_items.pianos_menu_items import PianosMenu
from gui.menu_items.lessons_menu_items import LessonsMenu
from gui.menu_items.music_theory.music_theory_menu_items import MusicTheoryMenu
from services.pianos.piano_service import PianoService
from services.lessons.lesson_service import LessonService
from services.tones.tone_service import ToneService
from services.scales.scale_service import ScaleService
from services.chords.chord_service import ChordService
from services.circles.circle_service import CircleService

class MainMenu:
    def __init__(self, config):
        pass
    
    def display(self):
        pass
    
    def pianos_menu(self):
        pass
    
    def music_theory_menu(self):
        pass
    
    def lessons_menu(self):
        pass
```


#### `gui/menu_items/__init__.py`

```python
from gui.menu_items.pianos_menu_items import PianosMenu
from gui.menu_items.lessons_menu_items import LessonsMenu

__all__ = ['PianosMenu', 'LessonsMenu']
```


#### `gui/menu_items/pianos_menu_items.py`

```python
class PianosMenu:
    def __init__(self, piano_service):
        self.service = piano_service
    
    def display(self):
        pass
    
    def list_all(self):
        pass
    
    def view_details(self):
        pass
    
    def add_piano(self):
        pass
    
    def update_piano(self):
        pass
    
    def delete_piano(self):
        pass
    
    def search_by_category(self):
        pass
    
    def search_by_manufacturer(self):
        pass
```


#### `gui/menu_items/lessons_menu_items.py`

```python
class LessonsMenu:
    def __init__(self, lesson_service):
        self.service = lesson_service
    
    def display(self):
        pass
    
    def list_all(self):
        pass
    
    def view_details(self):
        pass
    
    def add_lesson(self):
        pass
    
    def update_lesson(self):
        pass
    
    def delete_lesson(self):
        pass
    
    def filter_by_difficulty(self):
        pass
```


#### `gui/menu_items/music_theory/__init__.py`

```python
from gui.menu_items.music_theory.music_theory_menu_items import MusicTheoryMenu
from gui.menu_items.music_theory.tones_menu_items import TonesMenu
from gui.menu_items.music_theory.scales_menu_items import ScalesMenu
from gui.menu_items.music_theory.chords_menu_items import ChordsMenu
from gui.menu_items.music_theory.circles_menu_items import CirclesMenu

__all__ = [
    'MusicTheoryMenu',
    'TonesMenu',
    'ScalesMenu',
    'ChordsMenu',
    'CirclesMenu'
]
```


#### `gui/menu_items/music_theory/music_theory_menu_items.py`

```python
from gui.menu_items.music_theory.tones_menu_items import TonesMenu
from gui.menu_items.music_theory.scales_menu_items import ScalesMenu
from gui.menu_items.music_theory.chords_menu_items import ChordsMenu
from gui.menu_items.music_theory.circles_menu_items import CirclesMenu

class MusicTheoryMenu:
    def __init__(self, tone_service, scale_service, chord_service, circle_service):
        pass
    
    def display(self):
        pass
    
    def tones_menu(self):
        pass
    
    def scales_menu(self):
        pass
    
    def chords_menu(self):
        pass
    
    def circles_menu(self):
        pass
```


#### `gui/menu_items/music_theory/tones_menu_items.py`

```python
class TonesMenu:
    def __init__(self, tone_service):
        self.service = tone_service
    
    def display(self):
        pass
    
    def list_all(self):
        pass
    
    def view_details(self):
        pass
    
    def add_tone(self):
        pass
    
    def update_tone(self):
        pass
    
    def delete_tone(self):
        pass
```


#### `gui/menu_items/music_theory/scales_menu_items.py`

```python
class ScalesMenu:
    def __init__(self, scale_service):
        self.service = scale_service
    
    def display(self):
        pass
    
    def list_all(self):
        pass
    
    def view_details(self):
        pass
    
    def add_scale(self):
        pass
    
    def update_scale(self):
        pass
    
    def delete_scale(self):
        pass
```


#### `gui/menu_items/music_theory/chords_menu_items.py`

```python
class ChordsMenu:
    def __init__(self, chord_service):
        self.service = chord_service
    
    def display(self):
        pass
    
    def list_all(self):
        pass
    
    def view_details(self):
        pass
    
    def add_chord(self):
        pass
    
    def update_chord(self):
        pass
    
    def delete_chord(self):
        pass
```


#### `gui/menu_items/music_theory/circles_menu_items.py`

```python
class CirclesMenu:
    def __init__(self, circle_service):
        self.service = circle_service
    
    def display(self):
        pass
    
    def list_all(self):
        pass
    
    def view_details(self):
        pass
    
    def add_circle(self):
        pass
    
    def update_circle(self):
        pass
    
    def delete_circle(self):
        pass
```


***

### GLAVNI FAJLOVI

#### `config.py`

```python
class AppConfig:
    def __init__(self, data_dir, db_path, storage_type):
        self.data_dir = data_dir
        self.db_path = db_path
        self.storage_type = storage_type

def load_config():
    pass
```


#### `app.py`

```python
from config import load_config, AppConfig
from gui.main_menu import MainMenu

def main():
    pass

if __name__ == "__main__":
    main()
```


## Objašnjenje Strukture

### Core Paket

Sadrži sve modele (klase) koji predstavljaju entitete u sustavu.[^1][^2]

### Infrastructure Paket

Sadrži repozitorije koji upravljaju pohranjivanjem podataka u JSON datoteke.[^3][^1]

### Services Paket

Sadrži servise koji implementiraju poslovnu logiku i pozivaju repozitorije.[^2][^4]

### GUI Paket

Sadrži izborničke klase za interakciju s korisnikom.[^5][^1]

### __init__.py Fajlovi

Koriste se za definiranje paketa i olakšavanje importa. Svaki `__init__.py` uvozi klase iz svojih modula i definira `__all__` listu koja specificira što se izvozi.[^4][^1][^2][^3]

Ova struktura omogućava čistu separaciju odgovornosti i lakše održavanje koda.[^1][^5][^3]
<span style="display:none">[^10][^6][^7][^8][^9]</span>

<div align="center">⁂</div>

[^1]: https://realpython.com/python-init-py/

[^2]: https://www.geeksforgeeks.org/python/what-is-__init__-py-file-in-python/

[^3]: https://leapcell.io/blog/understanding-init-py-in-python-packages

[^4]: https://sentry.io/answers/what-is-init-py-for-in-python/

[^5]: https://timothybramlett.com/how-to-create-a-python-package-with-__init__-py/

[^6]: https://stackoverflow.com/questions/35727134/module-imports-and-init-py

[^7]: https://www.youtube.com/watch?v=VEbuZox5qC4

[^8]: https://www.reddit.com/r/learnpython/comments/1f565ru/what_can_i_put_in_init_py_to_make_them_useful/

[^9]: https://stackoverflow.com/questions/448271/what-is-init-py-for

[^10]: https://packaging.python.org/tutorials/packaging-projects/

