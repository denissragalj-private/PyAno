from config import AppConfig


def load_config() -> AppConfig:
    return AppConfig()


def main():
    config = load_config()
    # kreiraj db repo i pokreni GUI
    # repo = Repo(config)
    # Upotreba repozitorija na način:
    #    repo.ModelRepozitorij.crud_metoda()
    #    Primjer za modele Piano, PianoChategory
    #    repo.Piano.create(new_piano)
    #    repo.PianoCategory.create(new_piano_category)
    pass


if __name__ == "__main__":
    main()
