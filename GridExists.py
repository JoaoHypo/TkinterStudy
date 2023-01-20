from tkinter import *
import pandas as pd

root = Tk()

#Criando um widget label
myLabel1 = Label(root, text = "Hellow World!")
myLabel2 = Label(root, text = "Learning Grid")

#Jogando para o root, deste vez utilizando o sistema de GRID da GUI
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
#Como tem 1 gap de colunas vazias da 1 a 5 o tkinter ignora e plota como se fosse um column 0 e 1


#Por py ser object oriented podemos simplesmente declrar as coisas ja as exivindo na tela

Label(root, text = "no variable text ").grid(row=2, column=3)


root.mainloop()
