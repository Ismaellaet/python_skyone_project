class Squad:
    def __init__(self, name, techlead = None, devs = None):
        self.name = name
        self.techlead = techlead
        self.devs = []

    def set_techlead(self, techlead):
        self.techlead = techlead

    def add_dev(self, dev):
        self.devs.append(dev)