from entity.piece import Piece

class Player:
    def __init__(self, pieces: Piece, winner: bool):
        self.pieces = pieces

