class Piece:
    def __init__(self, finished: bool, identifier: int, location: int, state: int):
        self.finished = finished
        self.identifier = identifier
        self.location = location
        self.state = state

    def setFinished(self, finished: bool):
        self.finished = finished

    def getFinished(self):
        return self.finished

    def setIdentifier(self, identifier: int):
        self.identifier = identifier

    def getIdentifier(self):
        return self.identifier

    def setLocation(self, location: int):
        self.location = location

    def getLocation(self):
        return self.location

    def setState(self, state: int):
        self.state = state

    def getState(self):
        return self.state