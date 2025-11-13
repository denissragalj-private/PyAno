

DATABASE_PATH = 'data_store/db/py_ano.db'
NAME_LENGTH = 150


class AppConfig:
    def __init__(self, db_path: str = DATABASE_PATH):
        self.db_path = db_path
        
    

    # TODO kreirati metodu koja će pokrenuti u konstruktoru i
    # iz config.yaml učitati konfiguracijske postavke i ostale inicijalne postavke



def load_config() -> AppConfig:
    return AppConfig()

def main():
    config = load_config()
    # kreiraj db 
    pass


if __name__ == "__main__":
    main()
from config import AppConfig    
