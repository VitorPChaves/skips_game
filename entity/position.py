class Position:
    def __init__(self, occupied):
        self.occupied = occupied

    def setOccupied(self, occupied: bool):
        self.occupied = occupied

    def getOccupied(self):
        return  self.occupied
