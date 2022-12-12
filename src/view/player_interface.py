from dog.dog_actor import DogActor
from dog.dog_interface import DogPlayerInterface
from entity.player import Player
from entity.piece import Piece
from entity.board import Board
from tkinter import *
from tkinter import simpledialog, messagebox

import sys
sys.path.insert(0, '../src')


class ActorPlayer(DogPlayerInterface):
    def __init__(self):
        self.window = Tk()
        self.window.title('SKIPS')
        self.window.geometry('700x500')
        self.window.resizable(False, False)

        self.game_state = 2     # 1 = no match / 2 = match running blue turn / 3 = match running yellow turn / 4 = blue winner / 5 = yellow winner / 6 = withdrawal

        self.localPlayer = Player()
        self.remotePlayer = Player()

        self.b1_piece_button = Button(self.window, text="*", height=3, width=3,
                                      highlightbackground='#0000FF', command=lambda: self.move_piece(self.b1_piece))
        self.b2_piece_button = Button(self.window, text="**", height=3, width=3,
                                      highlightbackground='#0000FF', command=lambda: self.move_piece(self.b2_piece))
        self.b3_piece_button = Button(self.window, text="***", height=3, width=3,
                                      highlightbackground='#0000FF', command=lambda: self.move_piece(self.b3_piece))

        self.y1_piece_button = Button(self.window, text="#", height=3, width=3,
                                      highlightbackground='#F7EC3E', command=lambda: self.move_piece(self.y1_piece))
        self.y2_piece_button = Button(self.window, text="##", height=3, width=3,
                                      highlightbackground='#F7EC3E', command=lambda: self.move_piece(self.y2_piece))
        self.y3_piece_button = Button(self.window, text="###", height=3, width=3,
                                      highlightbackground='#F7EC3E', command=lambda: self.move_piece(self.y3_piece))

        self.b1_piece = Piece(False, 1, 1, 1, self.b1_piece_button)
        self.b2_piece = Piece(False, 2, 1, 1, self.b2_piece_button)
        self.b3_piece = Piece(False, 3, 1, 1, self.b3_piece_button)

        self.y1_piece = Piece(False, -1, 8, 1, self.y1_piece_button)
        self.y2_piece = Piece(False, -2, 8, 1, self.y2_piece_button)
        self.y3_piece = Piece(False, -3, 8, 1, self.y3_piece_button)

        self.pieces_data = []
        self.pieces_data.append(self.b1_piece)
        self.pieces_data.append(self.b2_piece)
        self.pieces_data.append(self.b3_piece)
        self.pieces_data.append(self.y1_piece)
        self.pieces_data.append(self.y2_piece)
        self.pieces_data.append(self.y3_piece)

        self.blue_pieces = []
        self.blue_pieces.append(self.b1_piece)
        self.blue_pieces.append(self.b2_piece)
        self.blue_pieces.append(self.b3_piece)

        self.yellow_pieces = []
        self.yellow_pieces.append(self.y1_piece)
        self.yellow_pieces.append(self.y2_piece)
        self.yellow_pieces.append(self.y3_piece)

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

        self.menu_file.add_command(
            label="Iniciar jogo", command=self.start_match)
        self.menu_file.add_command(
            label="Restaurar estado inicial", command=self.start_game)

        player_name = simpledialog.askstring(
            title="Player identification", prompt="Qual o seu nome?")
        self.dog_server_interface = DogActor()
        message = self.dog_server_interface.initialize(player_name, self)
        messagebox.showinfo(message=message)

        self.move_to_send = {}

        self.window.mainloop()

    def draw_board(self):
        # Adiciona as posições no tabuleiro para o tkinter não "comer" as posições depois de adicionar as peças
        for p in range(10):
            position = Button(self.window, text="-", height=3,
                              width=3, highlightbackground='#F0160F')
            position.grid(row=0, column=p)

        for p in range(6):
            position = Button(self.window, text="-", height=3,
                              width=3, highlightbackground='#F0160F')
            position.grid(row=1, column=(p+2))

        for p in range(6):
            position = Button(self.window, text="-", height=3,
                              width=3, highlightbackground='#F0160F')
            position.grid(row=3, column=(p+2))

        for p in range(10):
            position = Button(self.window, text="-", height=3,
                              width=3, highlightbackground='#F0160F')
            position.grid(row=4, column=p)

    def is_player_turn(self, piece):
        print(self.game_state)
        print(piece.getIdentifier())

        if self.game_state == 2 and piece.getIdentifier() > 0:
            return True
        if self.game_state == 2 and piece.getIdentifier() < 0:
            return False
        if self.game_state == 3 and piece.getIdentifier() > 0:
            return False
        if self.game_state == 3 and piece.getIdentifier() < 0:
            return True

    def piece_can_move(self, piece):

        if piece.getIdentifier() == 1 or piece.getIdentifier() == -1:
            if piece.getLocation() == 4 or piece.getLocation() == 5:
                return False
            else:
                return True

        elif piece.getIdentifier() == 2 or piece.getIdentifier() == -2:
            if piece.getLocation() == 3 or piece.getLocation() == 6:
                return False
            else:
                return True

        elif piece.getIdentifier() == 3 or piece.getIdentifier() == -3:
            if piece.getLocation() == 2 or piece.getLocation() == 7:
                return False
            else:
                return True
        else:
            return True

    def verify_destination(self, column: int):
        for piece in self.pieces_data:

            current_location = piece.getLocation()
            last_location = piece.getLocation()
            progress = 0

            if piece.getIdentifier() > 0:

                while progress < piece.getIdentifier():
                    progress += 1
                    current_location += 1
                    piece.setState(2)

                    if current_location > 0 and current_location < 9:

                        for p in self.board_places:
                            if p.get_position() == current_location:
                                if p.get_occupied() == True:
                                    current_location += 1

                        if current_location == 8 and progress == piece.getIdentifier():
                            current_location = 9
                            piece.setState(4)
                            print("Piece Finished!")
                            break

            elif piece.getIdentifier() < 0:

                while progress > piece.getIdentifier():
                    progress -= 1
                    current_location -= 1
                    piece.setState(2)

                    if current_location > 0 and current_location < 9:
                        for p in reversed(self.board_places):
                            if p.get_position() == current_location:
                                if p.get_occupied() == True:
                                    current_location -= 1

                        if current_location == 1 and progress == piece.getIdentifier():
                            current_location = 0
                            piece.setState(4)
                            print("Piece Finished!")
                            break

            if current_location == column:
                return current_location

    def move_piece(self, piece: Piece):
        if self.is_player_turn(piece) == True:

            current_location = piece.getLocation()
            last_location = piece.getLocation()
            progress = 0

            if piece.getIdentifier() > 0:
                while progress < piece.getIdentifier():
                    progress += 1
                    current_location += 1
                    piece.setState(2)

                    if current_location > 0 and current_location < 9:

                        for p in self.board_places:
                            if p.get_position() == current_location:
                                if p.get_occupied() == True:
                                    current_location += 1

                        if current_location == 8 and progress == piece.getIdentifier():
                            current_location = 9
                            piece.setState(4)
                            # print(piece.getState())
                            print("Piece Finished!")
                            break

                        elif current_location >= 8 and progress != piece.getIdentifier():
                            current_location = last_location
                            piece.setState(3)
                            print("Invalid Movement!")
                            return

            elif piece.getIdentifier() < 0:

                while progress > piece.getIdentifier():
                    progress -= 1
                    current_location -= 1
                    piece.setState(2)

                    if current_location > 0 and current_location < 9:
                        # reversed para percorrer o tabuleiro na direcao dos identificadores negativos
                        for p in reversed(self.board_places):
                            if p.get_position() == current_location:
                                if p.get_occupied() == True:
                                    current_location -= 1

                        if current_location == 1 and progress == piece.getIdentifier():
                            current_location = 0
                            piece.setState(4)
                            print("Piece Finished!")
                            break

                        elif current_location <= 1 and progress != piece.getIdentifier():
                            current_location = last_location
                            piece.setState(3)
                            print("Invalid Movement!")
                            return

            piece.setLocation(current_location)
            self.occupy_position(piece, last_location)
        elif self.is_player_turn(piece) == False:
            print("It's not your turn, wait the other player move")

        # self.verify_winner()

    def occupy_position(self, piece, last_location):
        #finished: bool, identifier: int, location: int, state: int, piece_button

        move_to_send = {}

        if self.piece_can_move(piece) == False:
            piece.setLocation(last_location)
            piece.setState(3)
            print("Invalid move! This Piece is Blocked!")

        # Se a peca pode mover...
        elif self.piece_can_move(piece) == True:

            # changes the occupation of board positions
            for p in self.board_places:
                if p.get_position() == last_location:
                    occupied = False
                    p.set_occupied(occupied)
                if p.get_position() == piece.getLocation():
                    occupied = True
                    p.set_occupied(occupied)

            # posiciona a peca
            move_to_send["piece_finished"] = str(piece.getFinished())
            move_to_send["piece_identifier"] = str(piece.getIdentifier())
            move_to_send["piece_location"] = str(piece.getLocation())
            move_to_send["piece_state"] = str(piece.getState())
            move_to_send["piece_button"] = str(piece.getPieceButton())
            move_to_send["match_status"] = "next"
            self.change_turn()
            self.dog_server_interface.send_move(move_to_send)
            self.update_grid(piece)
            self.verify_winner()

    def update_grid(self, piece):
        if piece.getState() != 1 and piece.getState() != 3:
            piece.getPieceButton().grid(row=2, column=piece.getLocation())

    def change_turn(self):
        if self.game_state == 2:
            self.game_state = 3
        elif self.game_state == 3:
            self.game_state = 2

    def start_match(self):
        start_status = self.dog_server_interface.start_match(2)
        message = start_status.get_message()
        messagebox.showinfo(message=message)

    def receive_start(self, start_status):
        message = start_status.get_message()
        messagebox.showinfo(message=message)

    def receive_move(self, a_move):
        piece = int(a_move["piece_identifier"])

        for p in self.pieces_data:
            if p.getIdentifier() == piece:
                self.move_piece(p)

    def start_game(self):
        match_status = self.game_state
        if match_status == 2 or match_status == 6:
            self.reset_game()

    def reset_game(self):
        for p in self.blue_pieces:
            p.setLocation(1)

        for p in self.yellow_pieces:
            p.setLocation(8)

        self.b1_piece_button.grid(row=1, column=self.b1_piece.getLocation())
        self.b2_piece_button.grid(row=2, column=self.b2_piece.getLocation())
        self.b3_piece_button.grid(row=3, column=self.b3_piece.getLocation())

        self.draw_board()

        self.y1_piece_button.grid(row=1, column=self.y1_piece.getLocation())
        self.y2_piece_button.grid(row=2, column=self.y2_piece.getLocation())
        self.y3_piece_button.grid(row=3, column=self.y3_piece.getLocation())

    def verify_winner(self):

        if self.b1_piece.getState() == 4 and self.b2_piece.getState() == 4 and self.b3_piece.getState() == 4:
            self.game_state = 4
            print("Player 1 won!")
        elif self.y1_piece.getState() == 4 and self.y2_piece.getState() == 4 and self.y3_piece.getState() == 4:
            self.game_state = 5
            print("Player 2 won!")
        elif self.b1_piece.getState() != 2 and self.b2_piece.getState() != 2 and self.b3_piece.getState() != 2 and \
                self.b1_piece.getState() != 1 and self.b2_piece.getState() != 1 and self.b3_piece.getState() != 1:
            self.game_state = 5
            print("Player 2 won!")
        elif self.y1_piece.getState() != 2 and self.y2_piece.getState() != 2 and self.y3_piece.getState() != 2 and \
                self.y1_piece.getState() != 1 and self.y2_piece.getState() != 1 and self.y3_piece.getState() != 1:
            self.game_state = 4
            print("Player 1 won!")

    def receive_withdrawal_notification(self):
        self.game_state = 6


ActorPlayer()
