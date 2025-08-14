import tkinter as tk
from tkinter import Frame, Label, Entry, Button

def calcular_imc():
    imc = float(peso.get()) / (float(altura.get()) ** 2)
    resultado['text'] = f'Seu IMC é: {imc:.2f}'
    print(f'Seu IMC é: {imc:.2f}')


janela = tk.Tk()


frame = Frame(janela, padx=40, pady=40)
frame.grid(column=1, row=1)

Label(frame, text='Para calcular o IMC digite os valores abaixo:', pady=40)\
    .grid(column=1, row=1, columnspan=2)

Label(frame, text='Qual é seu Peso (kg):').grid(row=2, column=1)
peso = Entry(frame)
peso.grid(row=2, column=2)

Label(frame, text='Qual é sua Altura (m):').grid(row=3, column=1)
altura = Entry(frame)
altura.grid(column=2, row=3)

Button(frame, text='Calcular', command=calcular_imc)\
    .grid(row=4, column=1, columnspan=2)

resultado = Label(frame, text="")
resultado.grid(column=1, row=5, columnspan=2)

janela.title("Calculadora de IMC")
janela.mainloop()
