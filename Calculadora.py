#Biblioteca tkinter
from tkinter import *
from tkinter import ttk
import math
import ctypes


# Oculta a janela do console no Windows
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

#Cores Padrão
cor1 = "#3b3b3b" #preta
cor2 = "#feffff" #branca
cor3 = "#37474f" #preta2
cor4 = "#ECEFF9" #cinza
cor5 = "#FFAB10" #laranja

#janela principal
janela =Tk()
janela.title("Calculadora")
janela.geometry("235x287")
janela.resizable(False, False)
janela.attributes('-fullscreen', False)
janela.config(bg=cor1)
janela.iconbitmap('icon.ico')
janela.eval('tk::PlaceWindow %s center' % janela.winfo_toplevel())

#frames
frame_tela = Frame(janela, width=300, height=56, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_cientifico = Frame(janela, width=300, height=86)
frame_cientifico.grid(row=1, column=0)

frame_corpo = Frame(janela, width=300, height=340)
frame_corpo.grid(row=2, column=0)

#funções operacionais
global todos_Valores

todos_Valores = ''
saida = StringVar()

#função de impressão de valores
def entrar_Valor(evento):
    global todos_Valores

    todos_Valores = todos_Valores + str(evento)
    saida.set(todos_Valores)

#função calcular
def calcular():
    global todos_Valores

    modulos = ['math.tan', 'math.sin', 'math.cos', 'math.sqrt', 'math.log', 'math.log10', 'math.e', 'math.pow', 'math.pi']

    for i in modulos:
        if i== 'math.tan':
            todos_Valores = todos_Valores.replace('tan', i)

        if i== 'math.sin':
            todos_Valores = todos_Valores.replace('sin', i)

        if i== 'math.cos':
            todos_Valores = todos_Valores.replace('cos', i)

        if i== 'math.sqrt':
            todos_Valores = todos_Valores.replace('√', i)

        if i== 'math.log':
            todos_Valores = todos_Valores.replace('log', i)

        if i== 'math.log10':
            todos_Valores = todos_Valores.replace('log10', i)

        if i== 'math.e':
            todos_Valores = todos_Valores.replace('e', i)

        if i== 'math.pow':
            todos_Valores = todos_Valores.replace('pow', i)

        if i== 'math.pi':
            todos_Valores = todos_Valores.replace('π', i)


    resultado = eval(todos_Valores)
    saida.set(resultado)

    todos_Valores = ''


def limpar():
    global todos_Valores
    todos_Valores = ''
    saida.set('')


#configuração do label_tela
label_tela = Label(frame_tela, textvariable=saida, width=16, height=2,  padx=7, anchor='e', bd=0, justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
label_tela.place(x=0, y=0)

#configuração do button_cientifico
b_0 = Button(frame_cientifico, text= 'tan', command=lambda:entrar_Valor('tan'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_0.place(x=0, y=0)
b_1 = Button(frame_cientifico, text= 'sin', command=lambda:entrar_Valor('sin'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_1.place(x=59, y=0)
b_2 = Button(frame_cientifico, text= 'cos', command=lambda:entrar_Valor('cos'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_2.place(x=2*59, y=0)
b_3 = Button(frame_cientifico, text= '√',  command=lambda:entrar_Valor('√'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_3.place(x=3*59, y=0)

b_4 = Button(frame_cientifico, text= 'log', command=lambda:entrar_Valor('log'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_4.place(x=0, y=29)
b_5 = Button(frame_cientifico, text= 'log10', command=lambda:entrar_Valor('log10'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_5.place(x=59, y=29)
b_6 = Button(frame_cientifico, text= 'e', command=lambda:entrar_Valor('e'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_6.place(x=2*59, y=29)
b_7 = Button(frame_cientifico, text= 'pow', command=lambda:entrar_Valor('pow'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_7.place(x=3*59, y=29)

b_8 = Button(frame_cientifico, text= 'π', command=lambda:entrar_Valor('π'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_8.place(x=0, y=2*29)
b_9 = Button(frame_cientifico, text= ',', command=lambda:entrar_Valor(','), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_9.place(x=59, y=2*29)
b_10 = Button(frame_cientifico, text= '(', command=lambda:entrar_Valor('('), width=6,  height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_10.place(x=2*59, y=2*29)
b_11 = Button(frame_cientifico, text= ')', command=lambda:entrar_Valor(')'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_11.place(x=3*59, y=2*29)

#configuração do button_corpo
b_12 = Button(frame_corpo, text= 'C', command=limpar, width=14, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor1)
b_12.place(x=0, y=0)
b_13 = Button(frame_corpo, text= '%', command=lambda:entrar_Valor('%'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor1)
b_13.place(x=2*59, y=0)
b_14 = Button(frame_corpo, text= '/', command=lambda:entrar_Valor('/'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor1)
b_14.place(x=3*59, y=0)

b_15 = Button(frame_corpo, text= '*', command=lambda:entrar_Valor('*'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor1)
b_15.place(x=3*59, y=29)
b_15 = Button(frame_corpo, text= '+', command=lambda:entrar_Valor('+'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor1)
b_15.place(x=3*59, y=2*29)
b_15 = Button(frame_corpo, text= '-', command=lambda:entrar_Valor('-'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor1)
b_15.place(x=3*59, y=3*29)
b_20 = Button(frame_corpo, text= '=', command=calcular, width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor5, fg=cor1)
b_20.place(x=3*59, y=4*29)

b_16 = Button(frame_corpo, text= '9', command=lambda:entrar_Valor('9'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_16.place(x=0, y=29)
b_17 = Button(frame_corpo, text= '8', command=lambda:entrar_Valor('8'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_17.place(x=59, y=29)
b_18 = Button(frame_corpo, text= '7', command=lambda:entrar_Valor('7'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_18.place(x=2*59, y=29)
b_19 = Button(frame_corpo, text= '6', command=lambda:entrar_Valor('6'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_19.place(x=0, y=2*29)
b_16 = Button(frame_corpo, text= '5', command=lambda:entrar_Valor('5'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_16.place(x=59, y=2*29)
b_17 = Button(frame_corpo, text= '4', command=lambda:entrar_Valor('4'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_17.place(x=2*59, y=2*29)
b_18 = Button(frame_corpo, text= '3', command=lambda:entrar_Valor('3'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_18.place(x=0, y=3*29)
b_19 = Button(frame_corpo, text= '2', command=lambda:entrar_Valor('2'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_19.place(x=59, y=3*29)
b_18 = Button(frame_corpo, text= '1', command=lambda:entrar_Valor('1'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_18.place(x=2*59, y=3*29)
b_19 = Button(frame_corpo, text= '0', command=lambda:entrar_Valor('0'), width=14, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_19.place(x=0, y=4*29)
b_19 = Button(frame_corpo, text= '.', command=lambda:entrar_Valor('.'), width=6, height=1, relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=cor1, fg=cor2)
b_19.place(x=2*59, y=4*29)



janela.mainloop()