from tkinter import *
from PIL import ImageTk, Image
from entity.board import Board
#import boardTable.png
#from tkmacosx import Button
#from tkinter import messagebox

class ActorPlayer:
    def __init__(self):
        self.window = Tk()
        self.window.title('SKIPS')
        self.window.geometry('600x400')
        self.window.resizable(False, False)

        self.board = Board([1, 2, 3, 4, 5, 6])

        # Parece que nenhum tipo de mudança de cor funciona direito no mac

        #self.window.configure(highlightbackground='#3E4149')
        #self.window.configure(bg='#3E4149')
        #self.window["bg"]="gray"

        # Tentando aplicar a imagem do tabuleiro como background com Pillow *NÃO FUNCIONOU NO MAC*

        #img = ImageTk.PhotoImage(Image.open("boardTable2.gif"))
        #img = ImageTk.PhotoImage(Image.open("boardTable.png"))
        #self.img = ImageTk.PhotoImage(Image.open("../assets/boardTable3.jpg"))

        # Tentando aplicar a imagem de fundo com canvas *NÃO FUNCIONOU NO MAC*

        #boardImage = PhotoImage(file="boardTable.png")
        #boardImage = PhotoImage(file="boardTable2.gif")

        #background_label = Label(self.window, image=self.img)
        #background_label.place(x=0, y=0, relwidth=1, relheight=1)

        #canvas = Canvas(window, width=1800, height=900)
        #canvas.pack()
        #canvas.create_image(0, 0, image=img, anchor="nw")
        #canvas.create_text(900, 700, text="Tabuleiro SKIPS")

        peca1 = Button(self.window, text="*", height=3, width=6, highlightbackground='#0000FF',
                       command=lambda: self.jogada(peca1))
        peca2 = Button(self.window, text="**", height=3, width=6, highlightbackground='#0000FF',
                       command=lambda: self.jogada(peca2))
        peca3 = Button(self.window, text="***", height=3, width=6, highlightbackground='#0000FF',
                       command=lambda: self.jogada(peca3))

        peca4 = Button(self.window, text="#", height=3, width=6, highlightbackground='#F7EC3E',
                       command=lambda: self.jogada(peca4))
        peca5 = Button(self.window, text="##", height=3, width=6, highlightbackground='#F7EC3E',
                       command=lambda: self.jogada(peca5))
        peca6 = Button(self.window, text="###", height=3, width=6, highlightbackground='#F7EC3E',
                       command=lambda: self.jogada(peca6))

        # Tentei colocar labels de texto para simular o tabuleiro mas as cores de fundo não aparecem no MAC
        # Por isso tentei inserir a imagem como background, mas também não funcionou
        # Esses labels servem para manter as linhas e colunas existentes mesmo sem o posicionamento das peças
        pos1 = Label(self.window, text="***", height=3, width=6, highlightbackground='#FA241B')
        pos2 = Label(self.window, text="**", height=3, width=6, highlightbackground='#FA241B')
        pos3 = Label(self.window, text="*", height=3, width=6, highlightbackground='#FA241B')
        pos4 = Label(self.window, text="*", height=3, width=6, highlightbackground='#FA241B')
        pos5 = Label(self.window, text="**", height=3, width=6, highlightbackground='#FA241B')
        pos6 = Label(self.window, text="***", height=3, width=6, highlightbackground='#FA241B')

        peca1.grid(row=0, column=0, padx=10)
        peca2.grid(row=1, column=0, padx=10)
        peca3.grid(row=2, column=0, padx=10)

        # Posicionamento do tabuleiro
        pos1.grid(row=0, column=1)
        pos2.grid(row=0, column=2)
        pos3.grid(row=0, column=3)
        pos4.grid(row=0, column=4)
        pos5.grid(row=0, column=5)
        pos6.grid(row=0, column=6)

        peca4.grid(row=0, column=7, padx=10)
        peca5.grid(row=1, column=7, padx=10)
        peca6.grid(row=2, column=7, padx=10)

        self.window.mainloop()

    def jogada(self, piece, player=False):
        if (piece["text"]=="*"):
            piece.grid(row=1, column=1)
            print(self.board.getPositions()[0])
            # if there is a piece. jump
            # player.map(pieces) if one piece is in same position, position+2 { while talvez }
            #if (self.board.getPositions().[0]):
        elif (piece["text"]=="**"):
            piece.grid(row=1, column=2)
        elif (piece["text"]=="***"):
            piece.grid(row=1, column=3)
        elif (piece["text"]=="#"):
            piece.grid(row=1, column=6)
        elif (piece["text"]=="##"):
            piece.grid(row=1, column=5)
        elif (piece["text"]=="###"):
            piece.grid(row=1, column=4)

ActorPlayer()


