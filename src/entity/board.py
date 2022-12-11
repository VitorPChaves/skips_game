class Board:
    def __init__(self, occupied: bool, position: int):
        self.occupied = occupied
        self.position = position

    def set_occupied(self, occupied: bool):
        self.occupied = occupied

    def set_position(self, position: int):
        self.position = position

    def get_occupied(self):
        return self.occupied

    def get_position(self):
        return self.position

