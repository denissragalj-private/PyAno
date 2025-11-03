<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# PyAno Project Implementation Guide

Based on your project structure and requirements, here's a comprehensive step-by-step guide to implement the PyAno application.[^1][^2][^3]

## Implementation Order

### 1. Define Core Models

Start by creating domain models in the `core` package. Each model should represent a business entity with its properties and basic validation.[^4]

**Example: `core/pianos/pianos.py`**

```python
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Piano:
    id: Optional[int]
    name: str
    category: str
    piano_type: str
    manufacturer: str
    price: float
    year: int
    deleted: bool = False  # Soft delete flag
    deleted_at: Optional[datetime] = None
    created_at: datetime = None
    updated_at: datetime = None
```

**Apply this pattern to all models:**

- `core/tones/` - Tone model
- `core/scales/` - Scale model
- `core/chords/` - Chord model
- `core/circles/` - Circle model
- `core/lessons/` - Lesson model


### 2. Create Base Repository

Create a base repository class for JSON storage that implements CRUD operations.[^5][^1]

**`infrastructure/base_repository.py`**

```python
import json
import os
from typing import List, Optional, TypeVar, Generic
from datetime import datetime

T = TypeVar('T')

class BaseJsonRepository(Generic[T]):
    def __init__(self, file_path: str, model_class):
        self.file_path = file_path
        self.model_class = model_class
        self._ensure_file_exists()
    
    def _ensure_file_exists(self):
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)
    
    def _read_all(self) -> List[dict]:
        with open(self.file_path, 'r') as f:
            return json.load(f)
    
    def _write_all(self, data: List[dict]):
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=2, default=str)
    
    def create(self, entity: T) -> T:
        data = self._read_all()
        entity_dict = self._to_dict(entity)
        entity_dict['id'] = self._get_next_id(data)
        entity_dict['created_at'] = datetime.now().isoformat()
        entity_dict['updated_at'] = datetime.now().isoformat()
        data.append(entity_dict)
        self._write_all(data)
        return self._from_dict(entity_dict)
    
    def get_by_id(self, entity_id: int) -> Optional[T]:
        data = self._read_all()
        for item in data:
            if item['id'] == entity_id and not item.get('deleted', False):
                return self._from_dict(item)
        return None
    
    def get_all(self, include_deleted: bool = False) -> List[T]:
        data = self._read_all()
        if include_deleted:
            return [self._from_dict(item) for item in data]
        return [self._from_dict(item) for item in data if not item.get('deleted', False)]
    
    def update(self, entity_id: int, updates: dict) -> Optional[T]:
        data = self._read_all()
        for item in data:
            if item['id'] == entity_id:
                item.update(updates)
                item['updated_at'] = datetime.now().isoformat()
                self._write_all(data)
                return self._from_dict(item)
        return None
    
    def soft_delete(self, entity_id: int) -> bool:
        data = self._read_all()
        for item in data:
            if item['id'] == entity_id:
                item['deleted'] = True
                item['deleted_at'] = datetime.now().isoformat()
                self._write_all(data)
                return True
        return False
    
    def _get_next_id(self, data: List[dict]) -> int:
        return max([item['id'] for item in data], default=0) + 1
    
    def _to_dict(self, entity: T) -> dict:
        return entity.__dict__ if hasattr(entity, '__dict__') else vars(entity)
    
    def _from_dict(self, data: dict) -> T:
        return self.model_class(**data)
```


### 3. Implement Specific Repositories

Create repositories for each model in the `infrastructure` package.[^2][^3]

**Example: `infrastructure/pianos/piano_repository.py`**

```python
from core.pianos.pianos import Piano
from infrastructure.base_repository import BaseJsonRepository

class PianoRepository(BaseJsonRepository[Piano]):
    def __init__(self, file_path: str):
        super().__init__(file_path, Piano)
    
    def get_by_category(self, category: str):
        all_pianos = self.get_all()
        return [p for p in all_pianos if p.category == category]
    
    def get_by_price_range(self, min_price: float, max_price: float):
        all_pianos = self.get_all()
        return [p for p in all_pianos if min_price <= p.price <= max_price]
```


### 4. Create Services

Services coordinate business logic and call repository methods.[^1][^4]

**Example: `services/pianos/piano_service.py`**

```python
from typing import List, Optional
from core.pianos.pianos import Piano
from infrastructure.pianos.piano_repository import PianoRepository

class PianoService:
    def __init__(self, data_dir: str):
        self.repository = PianoRepository(f"{data_dir}/files/pianos.json")
    
    def create_piano(self, name: str, category: str, piano_type: str, 
                     manufacturer: str, price: float, year: int) -> Piano:
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
    
    def get_piano(self, piano_id: int) -> Optional[Piano]:
        return self.repository.get_by_id(piano_id)
    
    def list_all_pianos(self) -> List[Piano]:
        return self.repository.get_all()
    
    def update_piano(self, piano_id: int, **kwargs) -> Optional[Piano]:
        return self.repository.update(piano_id, kwargs)
    
    def delete_piano(self, piano_id: int) -> bool:
        return self.repository.soft_delete(piano_id)
    
    def search_by_category(self, category: str) -> List[Piano]:
        return self.repository.get_by_category(category)
```


### 5. Build Configuration System

**`config.py`**

```python
from dataclasses import dataclass
import yaml

@dataclass
class AppConfig:
    data_dir: str
    db_path: str
    storage_type: str  # 'json' or 'db'

def load_config() -> AppConfig:
    with open('config.yaml', 'r') as f:
        config_data = yaml.safe_load(f)
    return AppConfig(**config_data)
```

**`config.yaml`**

```yaml
data_dir: "data_store"
db_path: "data_store/db/py_ano.db"
storage_type: "json"
```


### 6. Create GUI Menu System

Build an interactive console menu.[^6][^7]

**`gui/main_menu.py`**

```python
from services.pianos.piano_service import PianoService

class MainMenu:
    def __init__(self, config):
        self.config = config
        self.piano_service = PianoService(config.data_dir)
        # Initialize other services
    
    def display(self):
        while True:
            print("\n=== PyAno Main Menu ===")
            print("1. Pianos")
            print("2. Music Theory")
            print("3. Lessons")
            print("0. Exit")
            
            choice = input("\nSelect option: ")
            
            if choice == "1":
                self.pianos_menu()
            elif choice == "2":
                self.music_theory_menu()
            elif choice == "3":
                self.lessons_menu()
            elif choice == "0":
                break
    
    def pianos_menu(self):
        from gui.menu_items.pianos_menu_items import PianosMenu
        menu = PianosMenu(self.piano_service)
        menu.display()
```

**`gui/menu_items/pianos_menu_items.py`**

```python
class PianosMenu:
    def __init__(self, piano_service):
        self.service = piano_service
    
    def display(self):
        while True:
            print("\n=== Pianos Menu ===")
            print("1. List all pianos")
            print("2. View piano details")
            print("3. Add new piano")
            print("4. Update piano")
            print("5. Delete piano")
            print("0. Back")
            
            choice = input("\nSelect option: ")
            
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
            elif choice == "0":
                break
    
    def list_all(self):
        pianos = self.service.list_all_pianos()
        for piano in pianos:
            print(f"{piano.id}. {piano.name} - {piano.manufacturer} ({piano.year})")
    
    def add_piano(self):
        name = input("Name: ")
        category = input("Category: ")
        piano_type = input("Type: ")
        manufacturer = input("Manufacturer: ")
        price = float(input("Price: "))
        year = int(input("Year: "))
        
        piano = self.service.create_piano(name, category, piano_type, 
                                         manufacturer, price, year)
        print(f"Piano created with ID: {piano.id}")
    
    def delete_piano(self):
        piano_id = int(input("Enter piano ID to delete: "))
        if self.service.delete_piano(piano_id):
            print("Piano deleted successfully (soft delete)")
        else:
            print("Piano not found")
```


### 7. Complete app.py

**`app.py`**

```python
from config import load_config
from gui.main_menu import MainMenu

def main():
    config = load_config()
    menu = MainMenu(config)
    menu.display()

if __name__ == "__main__":
    main()
```


## Implementation Strategy

**Phase 1: Foundation (Days 1-2)**

- Create all model classes in `core/`
- Implement `BaseJsonRepository`
- Create `config.py` and `config.yaml`

**Phase 2: Data Layer (Days 3-4)**

- Implement all repositories in `infrastructure/`
- Add specific query methods for each repository
- Test CRUD operations

**Phase 3: Business Logic (Days 5-6)**

- Create all services in `services/`
- Implement business validation
- Test soft delete functionality[^8][^9]

**Phase 4: User Interface (Days 7-8)**

- Build main menu system
- Create sub-menus for each entity
- Connect menus to services
- Handle user input validation

**Phase 5: Testing \& Refinement (Days 9-10)**

- Test all CRUD operations
- Verify soft delete works correctly
- Add error handling
- Refine user experience


## Key Principles

**Soft Delete Implementation:** Models include `deleted` (boolean) and `deleted_at` (datetime) fields. Repository methods filter out deleted items by default.[^9][^8]

**Separation of Concerns:** Models contain data, repositories handle persistence, services contain business logic, and GUI handles user interaction.[^2][^4]

**Repository Pattern Benefits:** Decouples data access from business logic, making it easy to switch from JSON to database storage later.[^3][^1]

This structured approach ensures maintainable, testable code that follows established design patterns.[^4][^1][^2]
<span style="display:none">[^10]</span>

<div align="center">⁂</div>

[^1]: https://red-bird.readthedocs.io

[^2]: https://www.cosmicpython.com/book/chapter_02_repository.html

[^3]: https://klaviyo.tech/the-repository-pattern-e321a9929f82

[^4]: https://dev.to/manukanne/a-python-implementation-of-the-unit-of-work-and-repository-design-pattern-using-sqlmodel-3mb5

[^5]: https://github.com/Miksus/red-bird

[^6]: https://refactoring.guru/design-patterns/command

[^7]: https://mehrnoosh.hashnode.dev/command-design-pattern-and-its-implementation-in-python

[^8]: https://github.com/miguelgrinberg/sqlalchemy-soft-delete

[^9]: https://stackoverflow.com/questions/37922029/soft-delete-django-database-objects

[^10]: https://stackoverflow.com/questions/9699598/implementation-of-repository-pattern-in-python

