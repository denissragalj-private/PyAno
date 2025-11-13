from config import AppConfig


def load_config() -> AppConfig:
    return AppConfig()


def main():
    config = load_config()
    # Kreiraj db repo i pokreni GUI
    # repo = Repo(config)
    # Uporaba repozitorija na nacin:
    #   repo.ModelRepository.crud_methods
    #   Primjer za modele: Piano, PianoCategory
    #   repo.Piano.create(new_piano)
    #   repo.PianoCategory.create(new_piano_category)
    pass


if __name__ == "__main__":
    main()
