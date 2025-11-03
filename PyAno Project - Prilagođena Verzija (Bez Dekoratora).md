<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# PyAno Project - Prilagođena Verzija (Bez Dekoratora)

Razumijem! Evo prilagođenog rješenja koje koristi samo osnovne Python klase sa `__init__` metodom, bez korištenja dekoratora.[^1][^2]

## 1. Kreiraj Klase Modela (bez @dataclass)

### Primjer: `core/pianos/pianos.py`

```python
from datetime import datetime

class Piano:
    def __init__(self, id, name, category, piano_type, manufacturer, price, year, 
                 deleted=False, deleted_at=None, created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.category = category
        self.piano_type = piano_type
        self.manufacturer = manufacturer
        self.price = price
        self.year = year
        self.deleted = deleted
        self.deleted_at = deleted_at
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()
    
    def to_dict(self):
        """Pretvara objekt u dictionary za JSON pohranu"""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'piano_type': self.piano_type,
            'manufacturer': self.manufacturer,
            'price': self.price,
            'year': self.year,
            'deleted': self.deleted,
            'deleted_at': self.deleted_at.isoformat() if self.deleted_at else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    def __str__(self):
        return f"Piano({self.name}, {self.manufacturer}, {self.year})"
```


### Primjer: `core/tones/tones.py`

```python
from datetime import datetime

class Tone:
    def __init__(self, id, name, frequency, octave, 
                 deleted=False, deleted_at=None, created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.frequency = frequency
        self.octave = octave
        self.deleted = deleted
        self.deleted_at = deleted_at
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'frequency': self.frequency,
            'octave': self.octave,
            'deleted': self.deleted,
            'deleted_at': self.deleted_at.isoformat() if self.deleted_at else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
    def __str__(self):
        return f"Tone({self.name}, {self.frequency}Hz, Octave {self.octave})"
```


### Primjer: `core/chords/chords.py`

```python
from datetime import datetime

class Chord:
    def __init__(self, id, name, notes, chord_type, 
                 deleted=False, deleted_at=None, created_at=None, updated_at=None):
        self.id = id
        self.name = name
        self.notes = notes  # Lista nota, npr. ['C', 'E', 'G']
        self.chord_type = chord_type  # major, minor, diminished, itd.
        self.deleted = deleted
        self.deleted_at = deleted_at
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'notes': self.notes,
            'chord_type': self.chord_type,
            'deleted': self.deleted,
            'deleted_at': self.deleted_at.isoformat() if self.deleted_at else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
```


## 2. Bazni Repozitorij

### `infrastructure/base_repository.py`

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
        """Kreira direktorij i prazan JSON file ako ne postoji"""
        directory = os.path.dirname(self.file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump([], f)
    
    def _read_all(self):
        """Čita sve podatke iz JSON datoteke"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _write_all(self, data):
        """Piše sve podatke u JSON datoteku"""
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def _get_next_id(self, data):
        """Generira sljedeći ID"""
        if not data:
            return 1
        max_id = max(item['id'] for item in data)
        return max_id + 1
    
    def create(self, entity):
        """CREATE - Dodaje novi entitet"""
        data = self._read_all()
        entity.id = self._get_next_id(data)
        entity.created_at = datetime.now()
        entity.updated_at = datetime.now()
        
        data.append(entity.to_dict())
        self._write_all(data)
        return entity
    
    def get_by_id(self, entity_id):
        """READ - Dohvaća entitet po ID-u (isključuje obrisane)"""
        data = self._read_all()
        for item in data:
            if item['id'] == entity_id and not item.get('deleted', False):
                return self._dict_to_entity(item)
        return None
    
    def get_all(self, include_deleted=False):
        """READ - Dohvaća sve entitete"""
        data = self._read_all()
        entities = []
        for item in data:
            if include_deleted or not item.get('deleted', False):
                entities.append(self._dict_to_entity(item))
        return entities
    
    def update(self, entity_id, update_dict):
        """UPDATE - Ažurira entitet"""
        data = self._read_all()
        for item in data:
            if item['id'] == entity_id:
                item.update(update_dict)
                item['updated_at'] = datetime.now().isoformat()
                self._write_all(data)
                return self._dict_to_entity(item)
        return None
    
    def soft_delete(self, entity_id):
        """DELETE - Soft delete (označava kao obrisano)"""
        data = self._read_all()
        for item in data:
            if item['id'] == entity_id:
                item['deleted'] = True
                item['deleted_at'] = datetime.now().isoformat()
                self._write_all(data)
                return True
        return False
    
    def _dict_to_entity(self, data_dict):
        """Pretvara dictionary u objekt modela"""
        # Konverzija datetime stringova u datetime objekte
        if data_dict.get('created_at'):
            data_dict['created_at'] = datetime.fromisoformat(data_dict['created_at'])
        if data_dict.get('updated_at'):
            data_dict['updated_at'] = datetime.fromisoformat(data_dict['updated_at'])
        if data_dict.get('deleted_at'):
            data_dict['deleted_at'] = datetime.fromisoformat(data_dict['deleted_at'])
        
        return self.model_class(**data_dict)
```


## 3. Specifični Repozitoriji

### `infrastructure/pianos/piano_repository.py`

```python
from infrastructure.base_repository import BaseJsonRepository
from core.pianos.pianos import Piano

class PianoRepository(BaseJsonRepository):
    def __init__(self, file_path):
        super().__init__(file_path, Piano)
    
    def get_by_category(self, category):
        """Dohvaća klavire po kategoriji"""
        all_pianos = self.get_all()
        return [piano for piano in all_pianos if piano.category == category]
    
    def get_by_manufacturer(self, manufacturer):
        """Dohvaća klavire po proizvođaču"""
        all_pianos = self.get_all()
        return [piano for piano in all_pianos if piano.manufacturer == manufacturer]
    
    def get_by_price_range(self, min_price, max_price):
        """Dohvaća klavire u određenom cjenovnom rangu"""
        all_pianos = self.get_all()
        return [piano for piano in all_pianos 
                if min_price <= piano.price <= max_price]
```


### `infrastructure/tones/tone_repository.py`

```python
from infrastructure.base_repository import BaseJsonRepository
from core.tones.tones import Tone

class ToneRepository(BaseJsonRepository):
    def __init__(self, file_path):
        super().__init__(file_path, Tone)
    
    def get_by_octave(self, octave):
        """Dohvaća tonove po oktavi"""
        all_tones = self.get_all()
        return [tone for tone in all_tones if tone.octave == octave]
```


## 4. Servisi

### `services/pianos/piano_service.py`

```python
from infrastructure.pianos.piano_repository import PianoRepository
from core.pianos.pianos import Piano

class PianoService:
    def __init__(self, data_dir):
        self.repository = PianoRepository(f"{data_dir}/files/pianos.json")
    
    def create_piano(self, name, category, piano_type, manufacturer, price, year):
        """Kreira novi klavir"""
        piano = Piano(
            id=None,
            name=name,
            category=category,
            piano_type=piano_type,
            manufacturer=manufacturer,
            price=price,
            year=year
        )
        return self.repository.create(piano)
    
    def get_piano(self, piano_id):
        """Dohvaća klavir po ID-u"""
        return self.repository.get_by_id(piano_id)
    
    def list_all_pianos(self):
        """Dohvaća sve klavire"""
        return self.repository.get_all()
    
    def update_piano(self, piano_id, name=None, category=None, piano_type=None, 
                     manufacturer=None, price=None, year=None):
        """Ažurira klavir"""
        update_dict = {}
        if name:
            update_dict['name'] = name
        if category:
            update_dict['category'] = category
        if piano_type:
            update_dict['piano_type'] = piano_type
        if manufacturer:
            update_dict['manufacturer'] = manufacturer
        if price:
            update_dict['price'] = price
        if year:
            update_dict['year'] = year
        
        return self.repository.update(piano_id, update_dict)
    
    def delete_piano(self, piano_id):
        """Briše klavir (soft delete)"""
        return self.repository.soft_delete(piano_id)
    
    def search_by_category(self, category):
        """Pretraživanje po kategoriji"""
        return self.repository.get_by_category(category)
    
    def search_by_price(self, min_price, max_price):
        """Pretraživanje po cijeni"""
        return self.repository.get_by_price_range(min_price, max_price)
```


## 5. Konfiguracija

### `config.py`

```python
class AppConfig:
    def __init__(self, data_dir, db_path, storage_type):
        self.data_dir = data_dir
        self.db_path = db_path
        self.storage_type = storage_type

def load_config():
    """Učitava konfiguraciju"""
    return AppConfig(
        data_dir="data_store",
        db_path="data_store/db/py_ano.db",
        storage_type="json"
    )
```


## 6. GUI Menu

### `gui/menu_items/pianos_menu_items.py`

```python
class PianosMenu:
    def __init__(self, piano_service):
        self.service = piano_service
    
    def display(self):
        while True:
            print("\n" + "="*40)
            print("    PIANOS MENU")
            print("="*40)
            print("1. Lista svih klavira")
            print("2. Pregled pojedinog klavira")
            print("3. Dodaj novi klavir")
            print("4. Ažuriraj klavir")
            print("5. Obriši klavir")
            print("6. Pretraži po kategoriji")
            print("0. Nazad")
            print("="*40)
            
            choice = input("\nOdaberi opciju: ")
            
            if choice == "1":
                self.list_all()
            elif choice == "2":
                self.view_details()
            elif choice == "3":
                self.add_piano()
            elif choice == "4":
                self.update_piano()
            elif choice == "5":
                self.delete_piano()
            elif choice == "6":
                self.search_by_category()
            elif choice == "0":
                break
            else:
                print("Nevažeća opcija!")
    
    def list_all(self):
        print("\n--- LISTA KLAVIRA ---")
        pianos = self.service.list_all_pianos()
        if not pianos:
            print("Nema klavira u bazi.")
            return
        
        for piano in pianos:
            print(f"\nID: {piano.id}")
            print(f"Naziv: {piano.name}")
            print(f"Proizvođač: {piano.manufacturer}")
            print(f"Godina: {piano.year}")
            print(f"Cijena: {piano.price} EUR")
            print("-" * 30)
    
    def view_details(self):
        try:
            piano_id = int(input("Unesi ID klavira: "))
            piano = self.service.get_piano(piano_id)
            
            if piano:
                print(f"\n--- DETALJI KLAVIRA ---")
                print(f"ID: {piano.id}")
                print(f"Naziv: {piano.name}")
                print(f"Kategorija: {piano.category}")
                print(f"Tip: {piano.piano_type}")
                print(f"Proizvođač: {piano.manufacturer}")
                print(f"Cijena: {piano.price} EUR")
                print(f"Godina: {piano.year}")
            else:
                print("Klavir nije pronađen!")
        except ValueError:
            print("Nevažeći ID!")
    
    def add_piano(self):
        print("\n--- DODAJ NOVI KLAVIR ---")
        name = input("Naziv: ")
        category = input("Kategorija (Grand/Upright/Digital): ")
        piano_type = input("Tip: ")
        manufacturer = input("Proizvođač: ")
        
        try:
            price = float(input("Cijena (EUR): "))
            year = int(input("Godina proizvodnje: "))
            
            piano = self.service.create_piano(
                name, category, piano_type, manufacturer, price, year
            )
            print(f"\nKlavir uspješno dodan! ID: {piano.id}")
        except ValueError:
            print("Nevažeći unos cijene ili godine!")
    
    def update_piano(self):
        try:
            piano_id = int(input("Unesi ID klavira za ažuriranje: "))
            piano = self.service.get_piano(piano_id)
            
            if not piano:
                print("Klavir nije pronađen!")
                return
            
            print(f"\nTrenutni podaci: {piano.name}")
            print("Ostavi prazno za zadržavanje trenutne vrijednosti")
            
            name = input(f"Novi naziv [{piano.name}]: ") or None
            category = input(f"Nova kategorija [{piano.category}]: ") or None
            price_input = input(f"Nova cijena [{piano.price}]: ")
            price = float(price_input) if price_input else None
            
            updated = self.service.update_piano(piano_id, name=name, 
                                               category=category, price=price)
            if updated:
                print("Klavir uspješno ažuriran!")
            else:
                print("Greška pri ažuriranju!")
        except ValueError:
            print("Nevažeći unos!")
    
    def delete_piano(self):
        try:
            piano_id = int(input("Unesi ID klavira za brisanje: "))
            confirm = input(f"Jesi li siguran da želiš obrisati klavir ID {piano_id}? (da/ne): ")
            
            if confirm.lower() == "da":
                if self.service.delete_piano(piano_id):
                    print("Klavir uspješno obrisan (soft delete)!")
                else:
                    print("Klavir nije pronađen!")
        except ValueError:
            print("Nevažeći ID!")
    
    def search_by_category(self):
        category = input("Unesi kategoriju: ")
        pianos = self.service.search_by_category(category)
        
        if not pianos:
            print(f"Nema klavira u kategoriji '{category}'")
            return
        
        print(f"\n--- KLAVIRI U KATEGORIJI {category} ---")
        for piano in pianos:
            print(f"{piano.id}. {piano.name} - {piano.manufacturer}")
```


### `gui/main_menu.py`

```python
from gui.menu_items.pianos_menu_items import PianosMenu
from services.pianos.piano_service import PianoService

class MainMenu:
    def __init__(self, config):
        self.config = config
        self.piano_service = PianoService(config.data_dir)
    
    def display(self):
        while True:
            print("\n" + "="*40)
            print("    PyAno - Main Menu")
            print("="*40)
            print("1. Klaviri")
            print("2. Glazbena teorija")
            print("3. Lekcije")
            print("0. Izlaz")
            print("="*40)
            
            choice = input("\nOdaberi opciju: ")
            
            if choice == "1":
                self.pianos_menu()
            elif choice == "2":
                print("Music Theory - U izradi...")
            elif choice == "3":
                print("Lessons - U izradi...")
            elif choice == "0":
                print("Doviđenja!")
                break
            else:
                print("Nevažeća opcija!")
    
    def pianos_menu(self):
        menu = PianosMenu(self.piano_service)
        menu.display()
```


## 7. Glavni Program

### `app.py`

```python
from config import load_config
from gui.main_menu import MainMenu

def main():
    print("Dobrodošli u PyAno!")
    config = load_config()
    menu = MainMenu(config)
    menu.display()

if __name__ == "__main__":
    main()
```


## Redoslijed Implementacije

**Korak 1:** Kreiraj sve klase modela u `core/` paketu[^2][^3][^1]

**Korak 2:** Implementiraj `BaseJsonRepository` sa CRUD metodama[^4][^1]

**Korak 3:** Kreiraj specifične repozitorije koji nasljeđuju bazni[^5]

**Korak 4:** Implementiraj servise koji koriste repozitorije[^6]

**Korak 5:** Kreiraj menu sustav u GUI paketu[^1]

**Korak 6:** Poveži sve u `app.py`[^2]

## Ključne Razlike od Verzije sa @dataclass

Klasični pristup koristi `__init__` metodu za inicijalizaciju atributa. Svaki atribut mora biti eksplicitno postavljen sa `self.attribute = value`. Dodana je `to_dict()` metoda za konverziju u dictionary jer bez `@dataclass` ovo nije automatski generirano. Koristi se `super().__init__()` za pozivanje konstruktora roditeljske klase.[^7][^3][^8][^5][^4][^1][^2]

Ovaj pristup je jednostavniji i ne zahtijeva znanje o dekoratorima, što je idealno za početnike.[^3][^1][^2]
<span style="display:none">[^10][^9]</span>

<div align="center">⁂</div>

[^1]: https://www.geeksforgeeks.org/python/__init__-in-python/

[^2]: https://www.geeksforgeeks.org/python/constructors-in-python/

[^3]: https://mimo.org/glossary/python/class

[^4]: https://realpython.com/python-classes/

[^5]: https://realpython.com/python-class-constructor/

[^6]: https://docs.python.org/3/tutorial/classes.html

[^7]: https://dev.to/romeopeter/python-normal-classes-vs-data-classes-which-should-you-use-30ip

[^8]: https://stackoverflow.com/questions/73988573/what-does-dataclass-syntax-do-without-dataclass

[^9]: https://stackoverflow.com/questions/6578487/init-as-a-constructor

[^10]: https://www.youtube.com/watch?v=oE_dWWWqxQ0

