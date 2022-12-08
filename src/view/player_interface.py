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

        self.b1_piece = Piece(False, 1, 1, 1)
        self.b2_piece = Piece(False, 2, 1, 1)
        self.b3_piece = Piece(False, 3, 1, 1)

        self.y1_piece = Piece(False, -1, 8, 1)
        self.y2_piece = Piece(False, -2, 8, 1)
        self.y3_piece = Piece(False, -3, 8, 1)

        self.b1_piece_button = Button(self.window, text="*", height=3, width=3, highlightbackground='#0000FF', command=lambda: self.move(self.b1_piece_button, self.b1_piece))
        self.b2_piece_button = Button(self.window, text="**", height=3, width=3, highlightbackground='#0000FF', command=lambda: self.move(self.b2_piece_button, self.b2_piece))
        self.b3_piece_button = Button(self.window, text="***", height=3, width=3, highlightbackground='#0000FF', command=lambda: self.move(self.b3_piece_button, self.b3_piece))

        self.y1_piece_button = Button(self.window, text="#", height=3, width=3, highlightbackground='#F7EC3E', command=lambda: self.move(self.y1_piece_button, self.y1_piece))
        self.y2_piece_button = Button(self.window, text="##", height=3, width=3, highlightbackground='#F7EC3E', command=lambda: self.move(self.y2_piece_button, self.y2_piece))
        self.y3_piece_button = Button(self.window, text="###", height=3, width=3, highlightbackground='#F7EC3E', command=lambda: self.move(self.y3_piece_button, self.y3_piece))

        self.piecesInformations = []
        self.piecesInformations.append(self.b1_piece)
        self.piecesInformations.append(self.b2_piece)
        self.piecesInformations.append(self.b3_piece)
        self.piecesInformations.append(self.y1_piece)
        self.piecesInformations.append(self.y2_piece)
        self.piecesInformations.append(self.y3_piece)

        self.column2 = Board(False, 2)
        self.column3 = Board(False, 3)
        self.column4 = Board(False, 4)
        self.column5 = Board(False, 5)
        self.column6 = Board(False, 6)
        self.column7 = Board(False, 7)

        self.board_places = []
        self.board_places.append(self.column2)
        self.board_places.append(self.column3)
        self.board_places.append(self.column4)
        self.board_places.append(self.column5)
        self.board_places.append(self.column6)
        self.board_places.append(self.column7)

        self.b1_piece_button.grid(row=1, column=self.b1_piece.getLocation())
        self.b2_piece_button.grid(row=2, column=self.b2_piece.getLocation())
        self.b3_piece_button.grid(row=3, column=self.b3_piece.getLocation())

        self.draw_board()

        self.y1_piece_button.grid(row=1, column=self.y1_piece.getLocation())
        self.y2_piece_button.grid(row=2, column=self.y2_piece.getLocation())
        self.y3_piece_button.grid(row=3, column=self.y3_piece.getLocation())

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

    def move(self, piece_button, piece):

        if (piece_button["text"]=="*"):
            # keeps the piece in the correct column
            self.possible_moves(piece)
            self.update_grid(piece_button, piece)

        elif (piece_button["text"]=="**"):
            self.possible_moves(piece)
            self.update_grid(piece_button, piece)

        elif (piece_button["text"]=="***"):
            self.possible_moves(piece)
            self.update_grid(piece_button, piece)

        elif (piece_button["text"]=="#"):
            self.possible_moves(piece)
            self.update_grid(piece_button, piece)

        elif (piece_button["text"]=="##"):
            self.possible_moves(piece)
            self.update_grid(piece_button, piece)

        elif (piece_button["text"]=="###"):
            self.possible_moves(piece)
            """
            if piece.getState() == 1:
                piece_button.grid(row=3, column=piece.getLocation())
            else:
                piece_button.grid(row=2, column=piece.getLocation())  # RESOLVER b1_piece.getLocation()
            """
            self.update_grid(piece_button, piece)

    def piece_can_move(self, piece):
        # checar se a peça pode parar de se mover em determinada posição
        # if piece.identifier == 3 or piece.identifier == -3
            # piece.getPostion() == 4 or piece.getPosition() == 5
                # print("Movimento Invalido, peca bloqueada!")
                # devolve a peça para a ultima posicao
                # change state to movimento invalido
                # change state to piece blocked
                # if all pieces blocked player lost

        if piece.identifier == 1 or piece.identifier == -1:
            if piece.getLocation() == 4 or piece.getLocation() == 5:
                return False
            else:
                return True

        elif piece.identifier == 2 or piece.identifier == -2:
            if piece.getLocation() == 3 or piece.getLocation() == 6:
                return False
            else:
                return True

        elif piece.identifier == 3 or piece.identifier == -3:
            if piece.getLocation() == 2 or piece.getLocation() == 7:
                return False
            else:
                return True


    def possible_moves(self, piece: Piece):
        current_location = piece.getLocation()
        last_location = piece.getLocation()
        progress = 0
        board = [2, 3, 4, 5, 6, 7]

        if piece.identifier > 0:

            while progress < piece.identifier:
                progress += 1
                current_location += 1

                if current_location > 0 and current_location < 9:
                    """
                    for p in self.piecesInformations:
                        if p.getLocation() == current_location:
                            current_location += 1
                    """

                    # Fazer reverse para identifiers negativos
                    # Garantir que o reverse passa pela ordem correta
                    # Setar as posiçoes ocupadas para occupied true
                    for p in self.board_places:
                        if p.get_location == current_location:
                            if p.get_occupied == True:
                                current_location += 1

                    if current_location == 8 and progress == piece.identifier:
                        current_location = 9
                        print("Piece Finished!")
                        break

                    elif current_location >= 8 and progress != piece.identifier:
                        current_location = last_location
                        print("Invalid Movement!")
                        print(progress)
                        break


        elif piece.identifier < 0:

            while progress > piece.identifier:
                progress -= 1
                current_location -= 1

                if current_location > 0 and current_location < 9:
                    for p in self.piecesInformations:
                        successful = False
                        while not successful:
                            if p.getLocation() == current_location:
                                current_location -= 1

                    if current_location == 1 and progress == piece.identifier:
                        current_location = 0
                        print("Piece Finished!")
                        break

                    elif current_location <= 1 and progress != piece.identifier:
                        current_location = last_location
                        print("Invalid Movement!")
                        break

        piece.setLocation(current_location)
        piece.setState(2)

        if self.piece_can_move(piece) == False:
            piece.setLocation(last_location)
            print("Invalid move! This Piece is Blocked!")
            piece.setState(3)


        for p in self.piecesInformations:
            print(p.getLocation())

    def update_grid(self, piece_button, piece):
        if piece.getState() != 1 and piece.getState() != 3:
            piece_button.grid(row=2, column=piece.getLocation())

        """
        self.b1_piece_button.grid(column=self.b1_piece.getLocation())
        self.b2_piece_button.grid(column=self.b2_piece.getLocation())
        self.b3_piece_button.grid(column=self.b3_piece.getLocation())

        self.draw_board()

        self.y1_piece_button.grid(column=self.y1_piece.getLocation())
        self.y2_piece_button.grid(column=self.y2_piece.getLocation())
        self.y3_piece_button.grid(column=self.y3_piece.getLocation())
        """

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


