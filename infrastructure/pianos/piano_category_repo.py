from sqlalchemy.orm import Session

class PianoCategoryRepositoriy:
    def __init__(self, session: Session):
        self.session = session
    

    def get(self, piano_category: PianoCategory):
        pass

    def get_all(self, piano_category: PianoCategory):
        pass

    def add(self, piano_category: PianoCategory):
        pass

