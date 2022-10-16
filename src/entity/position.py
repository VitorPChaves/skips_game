class Position:
    def __init__(self, occupied: bool, identifier: int):
        self.occupied = occupied
        self.identifier = identifier

    def setOccupied(self, occupied: bool):
        self.occupied = occupied

    def getOccupied(self):
        return self.occupied

    def setIdentifier(self, identifier: int):
        self.identifier = identifier

    def getIdentifier(self):
        return self.identifier
