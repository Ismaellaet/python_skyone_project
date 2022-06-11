from Person import Person

class Contributor(Person):
    def __init__(self, name, phone, squad = None):
        super().__init__(name, phone)
        self.squad = squad

    def set_squad(self, squad):
        self.squad = squad