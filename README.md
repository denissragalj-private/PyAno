# PyAno

All about pianos and music theory

## Project folder structure

```
PyAno
|   .gitattributes
|   .gitignore
|   app.py
|   config.py
|   config.yaml
|   README.md
|   tree.txt
+---core
|   |   __init__.py
|   +---chords
|   |       __init__.py
|   +---circles
|   |       __init__.py
|   +---lessons
|   |       __init__.py
|   +---pianos
|   |       __init__.py
|   +---scales
|   |       __init__.py
|   \---tones
|           __init__.py
+---data_store
|   +---db
|   |       py_ano.db
|   \---files
|           chords.json
|           circles.json
|           lessons.json
|           pianos.json
|           scales.json
|           tones.json
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
