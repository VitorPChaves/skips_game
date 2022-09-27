class Piece:
    def __init__(self, finished: bool, identifier: int):
        self.finished = finished
        self.identifier = identifier

    def setFinished(self, finished: bool):
        self.finished = finished

    def getFinished(self):
        return self.finished