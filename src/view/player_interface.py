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
        self.board_state = 1

        self.localPlayer = Player()
        self.remotePlayer = Player()

        self.peca1 = Button(self.window, text="*", height=3, width=3, highlightbackground='#0000FF', command=lambda: self.move(self.peca1))
        self.peca2 = Button(self.window, text="**", height=3, width=3, highlightbackground='#0000FF', command=lambda: self.move(self.peca2))
        self.peca3 = Button(self.window, text="***", height=3, width=3, highlightbackground='#0000FF', command=lambda: self.move(self.peca3))

        self.peca4 = Button(self.window, text="#", height=3, width=3, highlightbackground='#F7EC3E', command=lambda: self.move(self.peca4))
        self.peca5 = Button(self.window, text="##", height=3, width=3, highlightbackground='#F7EC3E', command=lambda: self.move(self.peca5))
        self.peca6 = Button(self.window, text="###", height=3, width=3, highlightbackground='#F7EC3E', command=lambda: self.move(self.peca6))

        self.piece1 = Piece(False, 1, 1, 1)
        self.piece2 = Piece(False, 2, 1, 1)
        self.piece3 = Piece(False, 3, 1, 1)

        self.piece4 = Piece(False, -1, 8, 1)
        self.piece5 = Piece(False, -2, 8, 1)
        self.piece6 = Piece(False, -3, 8, 1)

        self.piecesInformations = []
        self.piecesInformations.append(self.piece1)
        self.piecesInformations.append(self.piece2)
        self.piecesInformations.append(self.piece3)
        self.piecesInformations.append(self.piece4)
        self.piecesInformations.append(self.piece5)
        self.piecesInformations.append(self.piece6)

        self.peca1.grid(row=1, column=self.piece1.getLocation())
        self.peca2.grid(row=2, column=self.piece2.getLocation())
        self.peca3.grid(row=3, column=self.piece3.getLocation())

        self.draw_board()

        self.peca4.grid(row=1, column=self.piece4.getLocation())
        self.peca5.grid(row=2, column=self.piece5.getLocation())
        self.peca6.grid(row=3, column=self.piece6.getLocation())

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

    def draw_board(self):
        # Adiciona as posições no tabuleiro para o tkinter não "comer" as posições depois de adicionar as peças
        for p in range(10):
            position = Button(self.window, text="-", height=3, width=3, highlightbackground='#F0160F')
            position.grid(row=0, column=p)

        for p in range(6):
            position = Button(self.window, text="-", height=3, width=3, highlightbackground='#F0160F')
            position.grid(row=1, column=(p+2))

        for p in range(6):
            position = Button(self.window, text="-", height=3, width=3, highlightbackground='#F0160F')
            position.grid(row=3, column=(p+2))

        for p in range(10):
            position = Button(self.window, text="-", height=3, width=3, highlightbackground='#F0160F')
            position.grid(row=4, column=p)

    def move(self, piece):


        if (piece["text"]=="*"):
            # garante que a peça vai ficar na linha do tabuleiro
            piece.grid(row=2, column=self.piece1.getLocation())  # RESOLVER piece1.getLocation()
            self.possible_moves(self.piece1)
            self.update_grid()

        elif (piece["text"]=="**"):
            # garante que a peça vai ficar na linha do tabuleiro
            piece.grid(row=2, column=self.piece2.getLocation())
            self.possible_moves(self.piece2)
            self.update_grid()

        elif (piece["text"]=="***"):
            # garante que a peça vai ficar na linha do tabuleiro
            piece.grid(row=2, column=self.piece3.getLocation())
            self.possible_moves(self.piece3)
            self.update_grid()

        elif (piece["text"]=="#"):
            # garante que a peça vai ficar na linha do tabuleiro
            piece.grid(row=2, column=self.piece4.getLocation())
            self.possible_moves(self.piece4)
            self.update_grid()

        elif (piece["text"]=="##"):
            # garante que a peça vai ficar na linha do tabuleiro
            piece.grid(row=2, column=self.piece5.getLocation())
            self.possible_moves(self.piece5)
            self.update_grid()

        elif (piece["text"]=="###"):
            # garante que a peça vai ficar na linha do tabuleiro
            piece.grid(row=2, column=self.piece6.getLocation())
            self.possible_moves(self.piece6)
            self.update_grid()


    def possible_moves(self, piece: Piece):
        current_location = piece.getLocation()
        last_location = piece.getLocation()
        progress = 0

        # if piece.identifier > 0
        # else if piece.identifier < 0

        """
        if (piece.identifier == 1):
            for i in range(1):
                current_location += 1
                # falta checar a quantidade de passos possíveis para a peça finalizar o tabuleiro
                if current_location == 7:
                    print("Piece Finished!")
                    # só para o botão sair do tabuleiro já que não encontrei uma função pra visibility
                    current_location = 9
                elif current_location < 7:
                    # checa se tem alguma peça na posição do tabuleiro, se tiver pula uma posiçao
                    for p in self.piecesInformations:
                        if p.getLocation() == current_location:
                            current_location += 1


        elif (piece.identifier == 2):
            for i in range(2):
                current_location += 1
                # falta checar a quantidade de passos possíveis para a peça finalizar o tabuleiro
                if current_location == 7 and i == 2:
                    print("Piece Finished!")
                    # só para o botão sair do tabuleiro já que não encontrei uma função pra visibility
                    current_location = 9
                    change_turn = True
                elif current_location == 7 and i < 2:
                    print("Movimento Invalido")
                    # change state to movimento invalido para alterar a mensagem
                    # change turn continua falso
                elif current_location < 7:
                    # checa se tem alguma peça na posição do tabuleiro, se tiver pula uma posiçao
                    for p in self.piecesInformations:
                        if p.getLocation() == current_location:
                            current_location += 1
            #piece.setLocation(current_location)
            # setChangeTurn(change_turn)

        elif (piece.identifier == 3):
            for i in range(3):
                current_location += 1
                # falta checar a quantidade de passos possíveis para a peça finalizar o tabuleiro
                if current_location == 7:
                    print("Piece Finished!")
                    # só para o botão sair do tabuleiro já que não encontrei uma função pra visibility
                    current_location = 9
                elif current_location < 7:
                    for p in self.piecesInformations:
                        if p.getLocation() == current_location:
                            current_location += 1
            #piece.setLocation(current_location)

        elif (piece.identifier == -1):
            for i in range(1):
                current_location -= 1
                # falta checar a quantidade de passos possíveis para a peça finalizar o tabuleiro
                if current_location == 1:
                    print("Piece Finished!")
                    # só para o botão sair do tabuleiro já que não encontrei uma função pra visibility
                    current_location = 0
                elif current_location > 0:
                    for p in self.piecesInformations:
                        if p.getLocation() == current_location:
                            current_location -= 1
            #piece.setLocation(current_location)

        elif (piece.identifier == -2):
            for i in range(2):
                current_location -= 1
                # falta checar a quantidade de passos possíveis para a peça finalizar o tabuleiro
                if current_location == 1:
                    print("Piece Finished!")
                    # só para o botão sair do tabuleiro já que não encontrei uma função pra visibility
                    current_location = 0
                elif current_location > 0:
                    for p in self.piecesInformations:
                        if p.getLocation() == current_location:
                            current_location -= 1
            #piece.setLocation(current_location)
        """

        if piece.identifier > 0:

            while progress < piece.identifier:
                progress += 1
                current_location += 1

                if current_location > 0 and current_location < 8:
                    for p in self.piecesInformations:

                        if p.getLocation() == current_location:
                            current_location += 1

                        elif current_location == 8 and progress == (piece.identifier):
                            current_location = 9
                            print("Piece Finished!")
                            break

                        elif current_location == 8 and progress > (piece.identifier):
                            current_location = last_location
                            print("Invalid Movement!")
                            break

        elif piece.identifier < 0:

            while progress > piece.identifier:
                progress -= 1
                current_location -= 1

                if current_location > 0 and current_location < 8:
                    for p in self.piecesInformations:
                        if p.getLocation() == current_location:
                            current_location -= 1

                        if current_location == 1 and progress == (piece.identifier):
                            current_location = 0
                            print("Piece Finished!")
                            break

                        elif current_location == 1 and progress > (piece.identifier):
                            current_location = last_location
                            print("Invalid Movement!")
                            break

        piece.setLocation(current_location)

        for p in self.piecesInformations:
            print(p.getLocation())

    def update_grid(self):

        self.peca1.grid(column=self.piece1.getLocation())
        self.peca2.grid(column=self.piece2.getLocation())
        self.peca3.grid(column=self.piece3.getLocation())

        self.draw_board()

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


