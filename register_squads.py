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

    def include_dev(self, dev):
        self.devs.append(dev)

class Contributor(Person):
    def __init__(self, name, phone, squad = None):
        super().__init__(name, phone)
        self.squad = squad

    def include_squad(self, squad):
        self.squad = squad

class Dev(Contributor):
    def __init__(self, name, phone, position, squad = None):
        super().__init__(name, phone, squad)
        self.position = position

squad_name = input('\n Squad name: ')
techlead_name = input(' Squad techlead\'s name: ')
techlead_phone = input(' Techlead\'s phone number: ')

squad = Squad(squad_name)
techlead = Contributor(techlead_name, techlead_phone)

squads = []
squads.append(squad) # Add squad in squads

squad.include_techlead(techlead)
techlead.include_squad(squad)
