from entity.position import Position

class Board:
    def __init__(self):
        """
        self.position1 = Position(False, 3)
        self.positions = [
            self.position1 = Position(False, 3), self.position2 = Position(False, 2), Position(False, 1)
        ]

        self.positions = []
        self.positions.append(Position(False, 3))
        self.positions.append(Position(False, 2))
        self.positions.append(Position(False, 1))
        self.positions.append(Position(False, 1))
        self.positions.append(Position(False, 2))
        self.positions.append(Position(False, 3))
        self.setPositions(self.positions)
        """



    def setPositions(self, positions):
        self.positions = positions

    def getPositions(self):
        return self.positions

    def checkConditions(self):
        return 0


