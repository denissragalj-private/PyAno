


DATABASE_PATH = 'sqlite:///data_store/db/py_ano.db'

# Models constraints
NAME_LENGHT = 150
DESCRIPTION_LENGHT = 1500
URL_LENGHT = 450
LOCATION_STR = 50


PIANO_CATEGORIES = ["Acoustic", "Electric", "Grand", "Upright", "Digital", "Hybrid"]
PIANO_TYPES = ["Acoustic", "Electric", "Digital", "Grand", "Upright"]


class AppConfig:
    def __init__(self, db_path: str = DATABASE_PATH):
        self.db_path = db_path

    # TODO Kreirati metodu koja ce se pokrenuti u kontruktoru
    # i iz config.yaml datoteke ucitati putanje i ostale inicijalne postavke
