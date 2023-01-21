# Video at current time: https://youtu.be/YXPyB4XeYLA?t=2603
from tkinter import *


root = Tk()
root.title('Calculadora Hypo')

entry = Entry(root, width=35,bg="Black",fg ="Green",borderwidth=15)
entry.grid(row=0, column=0, columnspan=3,padx=10,pady =10) #columnspan diz quantos espaços do grid tem que estender
#entry.insert(0,"") 


def button_add():
    return



butt1 = Button(root, text="1",bg="Black",fg ="Green",padx=40,pady=20, command=button_add)
butt1.grid(row=10)

root.mainloop()