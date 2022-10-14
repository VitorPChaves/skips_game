from entity.piece import Piece

class Player:
    def __init__(self):
        """
        self.pieces = pieces
        """
        #self.pieces = 3
        self.pieceOne = 1
        self.pieceTwo = 1
        self.pieceThree = 1
        self.turn = False
        self.winner = False

    def initialize(self):
        self.reset()

    def reset(self):
        self.pieces = 3
        self.turn = False
        self.winner = False

    def setTurn(self):
        if self.turn == False:
            self.turn = True
        elif self.turn == True:
            self.turn = False

    def getTurn(self):
        return self.turn

    def getWinner(self):
        return self.winner

    def setWinner(self):
        self.winner = True
