class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        print(f'\n-> {self.name} - {self.phone}')

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

    def __str__(self):
        super().__str__()
        return f'   {self.position} position in the {self.squad.name} squad'

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

        anotherDev = input('\n Want to add another dev [Y/N]: ')

        if anotherDev in 'Nn':
            break

    anotherSquad = input('\n Want to add another squad [Y/N]: ')

    if anotherSquad in 'Nn':
        break

for squad in squads:
    print(f'\n ------------------------------{squad.name}------------------------------')
    print(f' TeachLead: {squad.techlead.name}')
    print('\n -----Squad Developers-----')

    for dev in squad.devs:
        print(dev)