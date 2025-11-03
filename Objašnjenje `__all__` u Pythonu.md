<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Objašnjenje `__all__` u Pythonu

## Što je `__all__`?

`__all__` je **specijalna varijabla** koja se definira kao **lista stringova** i kontrolira što se izvozi iz modula ili paketa kada netko koristi `from module import *`.[^1][^3][^4]

```python
__all__ = ['Piano', 'PianoCategory', 'PianoType']
```


## Kako funkcionira?

Kada definirate `__all__` u modulu, samo imena navedena u toj listi će biti dostupna pri korištenju wildcard importa (*).[^2][^4][^1]

### Primjer bez `__all__`:

**modul.py:**

```python
def javna_funkcija():
    pass

def _privatna_funkcija():
    pass

pomocna_varijabla = 42
```

**drugi_modul.py:**

```python
from modul import *
# Uvozi SE: javna_funkcija, pomocna_varijabla
# NE uvozi se: _privatna_funkcija (jer počinje s _)
```


### Primjer SA `__all__`:

**modul.py:**

```python
__all__ = ['javna_funkcija']

def javna_funkcija():
    pass

def _privatna_funkcija():
    pass

pomocna_varijabla = 42
```

**drugi_modul.py:**

```python
from modul import *
# Uvozi se SAMO: javna_funkcija
# NE uvozi se: pomocna_varijabla, _privatna_funkcija
```


## Zašto koristiti `__all__`?

### 1. Sigurnost i Kontrola

Možete kontrolirati koji dijelovi koda su **javni API** (public interface) a koji su **interno** implementacijski detalji.[^3][^4][^1]

### 2. Sprječavanje Zagađenja Namespace-a

Sprječava uvoz nepotrebnih imena koja mogu sukobiti s postojećim imenima.[^4][^5]

### 3. Dokumentacija

Jasno pokazuje **što je namijenjeno za korištenje izvana** a što je interno.[^6][^4]

### 4. Čitljivost Koda

Drugi programeri mogu brzo vidjeti koji objekti čine javni API bez pregledavanja cijelog koda.[^7][^4]

## Primjeri iz Tvog PyAno Projekta

### `core/pianos/__init__.py`

```python
from core.pianos.piano import Piano
from core.pianos.piano_category import PianoCategory
from core.pianos.piano_type import PianoType

__all__ = ['Piano', 'PianoCategory', 'PianoType']
```

**Što ovo znači:**

- Kada netko napiše `from core.pianos import *`, uvest će se **samo** `Piano`, `PianoCategory` i `PianoType`
- Sve ostale varijable ili funkcije koje možda postoje u paketu **neće se uvesti**


### `services/__init__.py`

```python
from services.pianos.piano_service import PianoService
from services.tones.tone_service import ToneService

__all__ = ['PianoService', 'ToneService', ...]
```

**Što ovo znači:**

- Definiraš koje servise želiš da budu javno dostupni
- Interno možeš imati helper funkcije koje nisu u `__all__` i neće biti iznesene


## Važne Napomene

### `__all__` NE SPRJEČAVA direktni import

Ako netko napiše:[^1][^4]

```python
from core.pianos.piano import nesto_sto_nije_u_all
```

Ovo **će raditi** jer `__all__` utječe **samo** na `import *`.[^4][^1]

### Preporuke za korištenje

**1. Uvijek definiraj `__all__`** u svojim modulima i paketima[^5][^4]

**2. Drži `__all__` fokusiranim** - uključi samo javni API[^4]

**3. Ažuriraj `__all__`** kada dodaješ ili uklanjjaš javne funkcije/klase[^4]

**4. Koristi ga konzistentno** kroz cijeli projekt[^4]

## Praktični Primjer za PyAno

**Prije (bez `__all__`):**

```python
# core/pianos/__init__.py
from core.pianos.piano import Piano
from core.pianos.piano_category import PianoCategory

# Netko drugi:
from core.pianos import *
# Uvozi sve što je definirano, može biti zbunjujuće
```

**Poslije (sa `__all__`):**

```python
# core/pianos/__init__.py
from core.pianos.piano import Piano
from core.pianos.piano_category import PianoCategory

__all__ = ['Piano', 'PianoCategory']

# Netko drugi:
from core.pianos import *
# Uvozi SAMO Piano i PianoCategory - jasno i kontrolirano!
```


## Zaključak

`__all__` je **kontrolna lista** koja definira javni API tvog modula ili paketa. Iako nije obavezan, jako je koristan za pisanje čistog, sigurnog i profesionalnog koda. U tvom PyAno projektu, `__all__` osigurava da korisnici tvog koda znaju točno koje klase i funkcije su namijenjene za korištenje.[^3][^5][^6][^1][^4]
<span style="display:none">[^8]</span>

<div align="center">⁂</div>

[^1]: https://stackoverflow.com/questions/44834/what-does-all-mean-in-python

[^2]: https://www.bacancytechnology.com/qanda/python/what-dose-all-mean-in-python

[^3]: https://www.geeksforgeeks.org/python/python-__all__/

[^4]: https://realpython.com/python-all-attribute/

[^5]: https://www.esparkinfo.com/qanda/python/what-does-all-mean-in-python

[^6]: https://labex.io/ko/tutorials/python-how-to-use-all-in-module-definitions-450975

[^7]: https://labex.io/tutorials/python-how-to-use-all-in-python-modules-437148

[^8]: https://www.pmf.unizg.hr/_download/repository/RG_python.pdf

