__author__ = 'ThiagoAugustus'

import tkinter

from tkinter import *

app = tkinter.Tk()

#cria a area canvas
canvas = tkinter.Canvas(app, bg="gray", height=400, width = 600)
canvas.pack( side = TOP )

#cria os frames para organizar o conteudo
frame = Frame(app)
frame.pack()

#define as funcoes para manipulacao do canvas
def bandeira():
    limpar()
    # parametros x1, y1, x2, y2
    canvas.create_rectangle(100,50,500,350, outline="",fill="green")
    # parametros xn, yn por ponto
    canvas.create_polygon([300, 100, 450, 200, 300, 300, 150, 200], outline="",fill="yellow")
    # parametros x1, y1, x2, y2
    canvas.create_oval(250, 150, 350, 250, outline="", fill="blue")
def estrela():
    limpar()
    # parametros xn, yn por ponto
    #canvas.create_polygon([300,50, 350,150, 500,150, 390,240, 430,350, 300,290, 170,350, 210,240, 100,150, 250,150], outline="black",fill="",width=2)
    canvas.create_polygon([300,50, 440,350, 100,150, 500,150, 160,350], outline="",fill="white")
def limpar():
    canvas.delete("all")

labelMenu = Label(frame, text="Menu", fg="black", height=2, width=10)
labelMenu.pack( side = LEFT)

btnLimpar = Button(frame, text="Limpar", fg="red", height=2, width=10, command=limpar)
btnLimpar.pack( side = LEFT)

btnBandeira = Button(frame, text="Bandeira", fg="blue", height=2, width=10, command=bandeira)
btnBandeira.pack( side = RIGHT )

btnEstrela = Button(frame, text="Estrela", fg="blue", height = 2, width = 10, command=estrela)
btnEstrela.pack( side = RIGHT )

app.mainloop()