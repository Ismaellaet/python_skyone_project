class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Squad:
    def __init__(self, name, techlead = None, devs = None):
        self.name = name
        self.techlead = techlead
        self.devs = []

    def include_techlead(self, techlead):
        self.techlead = techlead

class Contributor(Person):
    def __init__(self, name, phone, squad = None):
        super().__init__(nome, phone)
        self.squad = squad
