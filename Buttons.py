from tkinter import *
import pandas as pd

root = Tk()

def myClick():
    mylabel = Label(root,text="clikcou >_< ")
    mylabel.pack()


#Medidas em pixels, state deixa não clicavel, podendo ser alterado chamando estado da classe!!!
MyButton = Button(root, text="me clicka UwU!", padx=50, pady=50,command=myClick, fg="pink",bg="green")
#Lembrar que em command não se finaliza as funções com (), porque sim.
#Fg - cor da fonte do texto
#bg - background color = can use hex color codes
MyButton.pack()

root.mainloop()