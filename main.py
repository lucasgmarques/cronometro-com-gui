from tkinter import *
import tkinter as tk

# cores
cor1 = "#0a0a0a"  # black / preta
cor2 = "#fafcff"  # white / branca
cor3 = "#21c25c"  # green / verde
cor4 = "#eb463b"  # red / vermelha
cor5 = "#dedcdc"  # gray / Cizenta
cor6 = "#3080f0"  # blue / azulri

janela = Tk()
janela.title("")
janela.geometry('315x180')
janela.resizable(width=FALSE, height=FALSE)
janela.configure(background=cor1)

# Definindo variáveis globais

global tempo
global rodar
global contador
global limitador

tempo = "00:00:00"
rodar = False
contador = -5
limitador = 59

def iniciar():
    global tempo
    global contador
    global limitador

    if rodar:
        # Antes do cronômetro iniciar
        if contador <=-1:
            inicio = 'Começando em ' +str(contador)
            label_tempo['text'] = inicio
            label_tempo['font'] = 'Arial 10'
        
        # Rodando o cronômetro
        else:
            label_tempo['font'] = 'Times 50 bold'
            
            novoTempo = str(tempo)
            horas,minutos,segundos = map(int,novoTempo.split(":"))
            horas = int(horas)
            minutos = int(minutos)
            segundos = int(contador)

            if (segundos>=limitador):
                contador = 0
                minutos += 1
            
            segundos = str(0)+str(segundos)
            minutos = str(0)+str(minutos)
            horas = str(0)+str(horas)
                

            # Atualizando os valores atuais
            novoTempo = str(horas[-2:]) + ":" + str(minutos[-2:]) + ":" + str(segundos[-2:])
            label_tempo['text'] = novoTempo
            tempo = novoTempo

        label_tempo.after(1000, iniciar)
        contador += 1

# Iniciar a função principal
def start():
    global rodar
    rodar = True
    iniciar()

# Função pausar
def pausar():
    global rodar
    rodar = False

# Função pausar
def reiniciar():
    global contador
    global tempo

    # Reiniciando o tempo
    contador = 0

    # Reiniciando o contador
    tempo = "00:00:00"
    label_tempo['text'] = tempo

# Criando os labels
label_app = Label(janela, text='Cronômetro', font=('Arial 10'), bg=cor1, fg=cor2)
label_app.place(x=20, y=5)

label_tempo = Label(janela, text=tempo, font=('Times 50 bold'), bg=cor1, fg=cor3)
label_tempo.place(x=20, y=40)

# Criando os Botões
botao_iniciar = Button(janela, command=start, text='Iniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_iniciar.place(x=20, y=120)

botao_pausar = Button(janela, command=pausar, text='Pausar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_pausar.place(x=115, y=120)

botao_reiniciar = Button(janela, command=reiniciar, text='Reiniciar', width=10, height=2, bg=cor1, fg=cor2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
botao_reiniciar.place(x=210, y=120)


janela.mainloop()
