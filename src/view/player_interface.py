from tkinter import *
from tkinter import simpledialog, messagebox

import sys
sys.path.insert(0, '../src')

from entity.board import Board
from entity.piece import Piece
from entity.player import Player

from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor

class ActorPlayer(DogPlayerInterface):
    def __init__(self):
        self.window = Tk()
        self.window.title('SKIPS')
        self.window.geometry('700x500')
        self.window.resizable(False, False)

        self.board = Board

        self.localPlayer = Player()
        self.remotePlayer = Player()

        self.peca1 = Button(self.window, text="*", height=3, width=6, highlightbackground='#0000FF', command=lambda: self.jogada(self.peca1))
        self.peca2 = Button(self.window, text="**", height=3, width=6, highlightbackground='#0000FF', command=lambda: self.jogada(self.peca2))
        self.peca3 = Button(self.window, text="***", height=3, width=6, highlightbackground='#0000FF', command=lambda: self.jogada(self.peca3))

        self.peca4 = Button(self.window, text="#", height=3, width=6, highlightbackground='#F7EC3E', command=lambda: self.jogada(self.peca4))
        self.peca5 = Button(self.window, text="##", height=3, width=6, highlightbackground='#F7EC3E', command=lambda: self.jogada(self.peca5))
        self.peca6 = Button(self.window, text="###", height=3, width=6, highlightbackground='#F7EC3E', command=lambda: self.jogada(self.peca6))

        self.piece1 = Piece(False, 1, 0)
        self.piece2 = Piece(False, 2, 0)
        self.piece3 = Piece(False, 3, 0)

        self.piece4 = Piece(False, -1, 7)
        self.piece5 = Piece(False, -2, 7)
        self.piece6 = Piece(False, -3, 7)

        """
        # foi a forma mais decente que encontrei de tirar o botão do tabuleiro
        self.finishedPiecesP1 = Button(self.window, text="X", height=3, width=6)
        self.finishedPiecesP1.grid(row=4, column=3, padx=10)
        self.finishedPiecesP2 = Button(self.window, text="X", height=3, width=6)
        self.finishedPiecesP2.grid(row=4, column=4, padx=10)
        """

        self.piecesInformations = []
        self.piecesInformations.append(self.piece1)
        self.piecesInformations.append(self.piece2)
        self.piecesInformations.append(self.piece3)
        self.piecesInformations.append(self.piece4)
        self.piecesInformations.append(self.piece5)
        self.piecesInformations.append(self.piece6)

        self.peca1.grid(row=0, column=self.piece1.getLocation(), padx=10)
        self.peca2.grid(row=1, column=self.piece2.getLocation(), padx=10)
        self.peca3.grid(row=2, column=self.piece3.getLocation(), padx=10)

        self.drawBoard()

        self.peca4.grid(row=0, column=self.piece4.getLocation(), padx=10)
        self.peca5.grid(row=1, column=self.piece5.getLocation(), padx=10)
        self.peca6.grid(row=2, column=self.piece6.getLocation(), padx=10)

        # Cria uma menu bar para poder iniciar a partida
        self.menubar = Menu(self.window)
        self.menubar.option_add("*tearOff", FALSE)
        self.window["menu"] = self.menubar

        self.menu_file = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menu_file, label="File")

        self.menu_file.add_command(label="Iniciar jogo", command=self.start_match)
        self.menu_file.add_command(label="Restaurar estado inicial", command=self.start_game)

        player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
        self.dog_server_interface = DogActor()
        message = self.dog_server_interface.initialize(player_name, self)
        messagebox.showinfo(message=message)

        self.window.mainloop()

    def drawBoard(self):
        # Adiciona as posições no tabuleiro para o tkinter não "comer" as posições depois de adicionar as peças
        for p in range(6):
            position = Label(self.window, text="*", height=3, width=6, highlightbackground='#FA241B')
            position.grid(row=0, column=(p+1))

    def jogada(self, piece):
        if (piece["text"]=="*"):
            #garante que a peça vai ficar na linha do tabuleiro
            piece.grid(row=1, column=self.piece1.getLocation())
            self.possibleMoves(self.piece1)
            self.updateGrid()

        elif (piece["text"]=="**"):
            # garante que a peça vai ficar na linha do tabuleiro
            piece.grid(row=1, column=self.piece2.getLocation())
            self.possibleMoves(self.piece2)
            self.updateGrid()

        elif (piece["text"]=="***"):
            # garante que a peça vai ficar na linha do tabuleiro
            piece.grid(row=1, column=self.piece3.getLocation())
            self.possibleMoves(self.piece3)
            self.updateGrid()

        elif (piece["text"]=="#"):
            # garante que a peça vai ficar na linha do tabuleiro
            piece.grid(row=1, column=self.piece4.getLocation())
            self.possibleMoves(self.piece4)
            self.updateGrid()

        elif (piece["text"]=="##"):
            # garante que a peça vai ficar na linha do tabuleiro
            piece.grid(row=1, column=self.piece5.getLocation())
            self.possibleMoves(self.piece5)
            self.updateGrid()

        elif (piece["text"]=="###"):
            # garante que a peça vai ficar na linha do tabuleiro
            piece.grid(row=1, column=self.piece6.getLocation())
            self.possibleMoves(self.piece6)
            self.updateGrid()

    """
    def checkConditions(self, piece, location: Location):
        if (piece["text"]=="**"):
            nextLocation = self.possibleMoves(piece)
            if self.piece2.getLocation() == 2 or self.piece2.getLocation() == 5:
                self.window.messagebox.showinfo(title=None, message="Invalid Move")
                print("Invalid Move")
                return False
        return True
    """

    def possibleMoves(self, piece: Piece):
        currentLocation = piece.getLocation()

        if (piece.identifier == 1):
            for i in range(1):
                currentLocation += 1
                # falta checar a quantidade de passos possíveis para a peça finalizar o tabuleiro
                if currentLocation == 7:
                    print("Piece Finished!")
                    # só para o botão sair do tabuleiro já que não encontrei uma função pra visibility
                    currentLocation = 20
                elif currentLocation < 7:
                    for p in self.piecesInformations:
                        if p.getLocation() == currentLocation:
                            currentLocation += 1
            piece.setLocation(currentLocation)

        elif (piece.identifier == 2):
            for i in range(2):
                currentLocation += 1
                # falta checar a quantidade de passos possíveis para a peça finalizar o tabuleiro
                if currentLocation == 7:
                    print("Piece Finished!")
                    # só para o botão sair do tabuleiro já que não encontrei uma função pra visibility
                    currentLocation = 20
                elif currentLocation < 7:
                    for p in self.piecesInformations:
                        if p.getLocation() == currentLocation:
                            currentLocation += 1
            piece.setLocation(currentLocation)

        elif (piece.identifier == 3):
            for i in range(3):
                currentLocation += 1
                # falta checar a quantidade de passos possíveis para a peça finalizar o tabuleiro
                if currentLocation == 7:
                    print("Piece Finished!")
                    # só para o botão sair do tabuleiro já que não encontrei uma função pra visibility
                    currentLocation = 20
                elif currentLocation < 7:
                    for p in self.piecesInformations:
                        if p.getLocation() == currentLocation:
                            currentLocation += 1
            piece.setLocation(currentLocation)

        elif (piece.identifier == -1):
            for i in range(1):
                currentLocation -= 1
                # falta checar a quantidade de passos possíveis para a peça finalizar o tabuleiro
                if currentLocation == 0:
                    print("Piece Finished!")
                    # só para o botão sair do tabuleiro já que não encontrei uma função pra visibility
                    currentLocation = 20
                elif currentLocation > 0:
                    for p in self.piecesInformations:
                        if p.getLocation() == currentLocation:
                            currentLocation -= 1
            piece.setLocation(currentLocation)

        elif (piece.identifier == -2):
            for i in range(2):
                currentLocation -= 1
                # falta checar a quantidade de passos possíveis para a peça finalizar o tabuleiro
                if currentLocation == 0:
                    print("Piece Finished!")
                    # só para o botão sair do tabuleiro já que não encontrei uma função pra visibility
                    currentLocation = 20
                elif currentLocation > 0:
                    for p in self.piecesInformations:
                        if p.getLocation() == currentLocation:
                            currentLocation -= 1
            piece.setLocation(currentLocation)

        elif (piece.identifier == -3):
            for i in range(3):
                currentLocation -= 1
                # falta checar a quantidade de passos possíveis para a peça finalizar o tabuleiro
                if currentLocation == 0:
                    print("Piece Finished!")
                    # só para o botão sair do tabuleiro já que não encontrei uma função pra visibility
                    currentLocation = 20
                elif currentLocation > 0:
                    for p in self.piecesInformations:
                        if p.getLocation() == currentLocation:
                            currentLocation -= 1
            piece.setLocation(currentLocation)

    def updateGrid(self):

        self.peca1.grid(column=self.piece1.getLocation())
        self.peca2.grid(column=self.piece2.getLocation())
        self.peca3.grid(column=self.piece3.getLocation())

        self.drawBoard()

        self.peca4.grid(column=self.piece4.getLocation())
        self.peca5.grid(column=self.piece5.getLocation())
        self.peca6.grid(column=self.piece6.getLocation())

    def start_match(self):
        start_status = self.dog_server_interface.start_match(2)
        message = start_status.get_message()
        messagebox.showinfo(message=message)

    def receive_start(self, start_status):
        message = start_status.get_message()
        messagebox.showinfo(message=message)

    def start_game(self):
        return 0

ActorPlayer()


