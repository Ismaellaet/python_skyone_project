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

squads = [] # Squads list

while True:
    squad_name = input('\n Squad name: ')
    techlead_name = input(' Squad techlead\'s name: ')
    techlead_phone = input(' Techlead\'s phone number: ')

    squad = Squad(squad_name)
    techlead = Contributor(techlead_name, techlead_phone)

    squad.include_techlead(techlead)
    techlead.include_squad(squad)

    squads.append(squad)  # Add squad in squads

    while True:
        dev_name = input('\n Dev\'s name: ')
        dev_phone = input(' Dev\'s phone number: ')
        dev_position = input(' Dev\'s position: ')

        dev = Dev(dev_name, dev_phone, dev_position)

        dev.include_squad(squad)
        squad.include_dev(dev)

        anotherDev = input('\nWant to add another dev [S/N]: ')

        if anotherDev in 'Nn':
            break

    anotherSquad = input('\nWant to add another squad [S/N]: ')

    if anotherSquad in 'Nn':
        break