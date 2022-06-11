from Contributor import Contributor

class Dev(Contributor):
    def __init__(self, name, phone, position, squad = None):
        super().__init__(name, phone, squad)
        self.position = position

    def __str__(self):
        super().__str__()
        return f'   Cargo de {self.position} na squad {self.squad.name}\n'