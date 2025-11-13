from pyfiglet import Figlet

from config import AppConfig
from infrastructure.base_repository import BaseRepository
from core.pianos.pianos import Piano


def load_config() -> AppConfig:
    return AppConfig()


def main():
    config = load_config()
    # Kreiraj db repo i pokreni GUI
    repo = BaseRepository()
    repo.db_seed()


    f = Figlet(font='slant')
    # Uporaba repozitorija na nacin:
    #   repo.ModelRepository.crud_methods
    #   Primjer za modele: Piano, PianoCategory
    #   repo.Piano.create(new_piano)
    #   repo.PianoCategory.create(new_piano_category)
    print(f.renderText('Pyano'))
    print()
    print()
    # print(repo.piano_category_repo.get_all())
    # print(repo.piano_type_repo.get_all())

    piano_cat_acustic = repo.piano_category_repo.get_by_name('Acustic')
    piano_type_grand = repo.piano_type_repo.get_by_name('Grand')
    piano = Piano(name='Steinway Grand',
                  price=5897258.99,
                  piano_category=piano_cat_acustic,
                  piano_type=piano_type_grand)
    # print("Piano prije DB", piano)
    # piano = repo.piano_repo.add(piano)
    # print("Piano poslije DB", piano)



if __name__ == "__main__":
    main()
