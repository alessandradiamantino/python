
from tkinter import *

# Guarda as configurações padrão para os
# botões que serão definidos mais tarde
button_default_config = {
    "font": "Arial 12 normal",
    "bg": "black",
    "fg": "white"
}


class Window(Frame):
    """ Janela principal """

    def __init__(self):
        """ Método construtor da janela"""
        super().__init__(master=None)  # Aqui iniciamos a nossa superclasse (Frame)

        # Definições de titulos, largura
        # e altura da janela principal
        self.master.geometry("300x200")
        self.master.title("n sei o que é")

        # Para os botões, definimos o texto e depois passamos o
        # dicionario de atributos usando "**" para o botão
        button1 = Button(self, text="clique para saber qual a melhor linguagem", **button_default_config)
        #button1 = print("é python")
        # Coloque cada botão em seu lugar e defina o
        # preenchimento dele usando o NSEW que significa
        # que o botão irá se ajustar ao tamanho dos items
        # ao seu redor e dentro da sua própria celula.
        button1.grid(row=100, column=0, pady=40, sticky=NSEW)

      
        # Essa é a parte mais importante, pois, define o
        # esticamento de cada celula do grid. Se possivel
        # comente as 2 linhas abaixo e teste para entender melhor
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Epacotamos o frame na janela
        self.pack(fill=BOTH, expand=True)


if __name__ == '__main__':
    window = Window()
    window.mainloop()
    print("é pyhton")