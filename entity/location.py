class Location:
    def __init__(self, line, column):
        self.line = line
        self.column = column

    def getLine(self):
        return self.line

    def getColumn(self):
        return self.column
