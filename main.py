__author__ = 'ThiagoAugustus'

import tkinter

from tkinter import *

class Desenho:

    app    = None
    frame  = None
    canvas = None

    def __init__(self):

        # Inicia o tkinter
        self.app = tkinter.Tk()

        # Cria a area canvas
        self.canvas = tkinter.Canvas(self.app, bg="gray", height=400, width = 600)
        self.canvas.pack( side = TOP )

        # Cria os frames para organizar o conteudo
        self.frame = Frame(self.app)
        self.frame.pack()

        # Adiciona os elementos
        self.componentes()

        # "Executável do programa"
        self.app.mainloop()

    # Define as funcoes para manipulacao do canvas
    def bandeira(self):
        self.limpar()
        # Parametros x1, y1, x2, y2
        self.canvas.create_rectangle(100,50,500,350, outline="",fill="green")
        # Parametros xn, yn por ponto
        self.canvas.create_polygon([300, 100, 450, 200, 300, 300, 150, 200], outline="",fill="yellow")
        # Parametros x1, y1, x2, y2
        self.canvas.create_oval(250, 150, 350, 250, outline="", fill="blue")
    def estrela(self):
        self.limpar()
        # Parametros xn, yn por ponto
        # Canvas.create_polygon([300,50, 350,150, 500,150, 390,240, 430,350, 300,290, 170,350, 210,240, 100,150, 250,150], outline="black",fill="",width=2)
        self.canvas.create_polygon([300,50, 440,350, 100,150, 500,150, 160,350], outline="",fill="white")
    def limpar(self):
        self.canvas.delete("all")

    # Componentes do painel
    def componentes(self):
        labelMenu = Label(self.frame, text="Menu", fg="black", height=2, width=10)
        labelMenu.pack( side = LEFT)

        btnLimpar = Button(self.frame, text="Limpar", fg="red", height=2, width=10, command=self.limpar)
        btnLimpar.pack( side = LEFT)

        btnBandeira = Button(self.frame, text="Bandeira", fg="blue", height=2, width=10, command=self.bandeira)
        btnBandeira.pack( side = RIGHT )

        btnEstrela = Button(self.frame, text="Estrela", fg="blue", height = 2, width = 10, command=self.estrela)
        btnEstrela.pack( side = RIGHT )

Desenho()