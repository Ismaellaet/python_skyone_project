class Person:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        print(f'-> {self.name} - {self.phone}')

class Squad:
    def __init__(self, name, techlead = None, devs = None):
        self.name = name
        self.techlead = techlead
        self.devs = []

    def set_techlead(self, techlead):
        self.techlead = techlead

    def add_dev(self, dev):
        self.devs.append(dev)

class Contributor(Person):
    def __init__(self, name, phone, squad = None):
        super().__init__(name, phone)
        self.squad = squad

    def set_squad(self, squad):
        self.squad = squad

class Dev(Contributor):
    def __init__(self, name, phone, position, squad = None):
        super().__init__(name, phone, squad)
        self.position = position

    def __str__(self):
        super().__str__()
        return f'   Cargo de {self.position} na squad {self.squad.name}\n'

squads = [] # Squads list

print('\n-==-=-=-=-=-=-=-=-=-=-=Sky.One Solutions=-=-=-=-=-=-=-=-=-=-')
print('Bem vindo ao sistema de cadastro de squads!\n')

# Loop to get all data
while True:
    squad_name = input('\n Nome da squad: ')
    techlead_name = input(' Nome do techlead da squad: ')

    squad = Squad(squad_name)
    techlead = Contributor(techlead_name, None)

    squad.set_techlead(techlead)
    techlead.set_squad(squad)

    squads.append(squad)  # Add squad in squads

    # Loop to get dev data
    while True:
        dev_name = input('\n Nome do desenvolvedor: ')
        dev_phone = input(' Telefone do desenvolvedor: ')
        dev_position = input(' Cargo do desenvolvedor: ')

        dev = Dev(dev_name, dev_phone, dev_position)

        dev.set_squad(squad)
        squad.add_dev(dev)

        anotherDev = input(' Deseja adicionar mais um dev? [S/N]: ')

        if anotherDev in 'Nn':
            break

    anotherSquad = input('\n Deseja adicionar mais uma squad? [S/N]: ')

    if anotherSquad in 'Nn':
        break

print('\n -==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')
print(' Squads criadas: ')

# Loop in squad list
for squad in squads:
    print(f'\n ------------------------------{squad.name}------------------------------')
    print(f' TeachLead: {squad.techlead.name}')
    print('\n -----Devs do squad-----')

    # Loop in the list of squad devs
    for dev in squad.devs:
        print(dev)

    print(f' ------------------------------{squad.name}------------------------------')

print('\n -==-=-=-=-=-=-=-=-=-=-=Sky.One Solutions=-=-=-=-=-=-=-=-=-=-=-=-=-=-')