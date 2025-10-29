# PyAno

All about pianos and music theory

## Project folder structure

``` bash
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
|   |       __init__.py
|   |       
|   +---circles
|   |       __init__.py
|   |       
|   +---lessons
|   |       __init__.py
|   |       
|   +---pianos
|   |       pianos.py
|   |       piano_categories.py
|   |       piano_types.py
|   |       __init__.py
|   |       
|   +---scales
|   |       __init__.py
|   |       
|   \---tones
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
|   |   __init__.py
|   |   
|   +---chords
|   |       __init__.py
|   |       
|   +---circles
|   |       __init__.py
|   |       
|   +---lessons
|   |       __init__.py
|   |       
|   +---pianos
|   |       __init__.py
|   |       
|   +---scales
|   |       __init__.py
|   |       
|   \---tones
|           __init__.py
|           
+---services
|   |   __init__.py
|   |   
|   +---chords
|   |       __init__.py
|   |       
|   +---circles
|   |       __init__.py
|   |       
|   +---lessons
|   |       __init__.py
|   |       
|   +---pianos
|   |       __init__.py
|   |       
|   +---scales
|   |       __init__.py
|   |       
|   \---tones
|           __init__.py
|           
\---venv
```

## Zadatak

- Kreirati klase za sve modele unutar core paketa.
- Kreirati klase repozitorija za pohranu svih modela unutar .json datoteka. Naziv .json datoteke treba biti *naziv_modela.json*.
- Kreirati servise za svaki model tako da servis poziva CRUD (Create, Read, Update, Delete) metode iz repozitorija. Kod inicijalizacije servisa, treba definirati da se koristi pohrana u .json datoteke.
- Unutar GUI paketa kreirati izbornike i ovisno o izboru korisnika pozivati odgovarajuću metodu iz servisa kako bi se prikazao jedan ili lista entiteta. Isto virjedi i za brisanje i ažuriranje. Brisanje ne briše iz baze nego se koristi *soft delete*.
