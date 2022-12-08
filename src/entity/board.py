class Board:
    def __init__(self, occupied: bool, position: int):
        self.occupied = occupied
        self.position = position

    def set_occupied(self, occupied):
        self.occupied = occupied

    def set_position(self, position):
        self.position = position

    def get_occupied(self):
        return self.occupied

    def get_position(self):
        return self.position

