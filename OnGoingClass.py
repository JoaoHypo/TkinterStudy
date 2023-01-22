# Video at current time: 

from tkinter import *

root = Tk()
root.title('Calculadora Hypo')

entry = Entry(root, width=35,bg="Black",fg ="Green",borderwidth=15)
entry.grid(row=0, column=0, columnspan=3,padx=10,pady =10) #columnspan diz quantos espaços do grid tem que estender
#entry.insert(0,"") 


def button_add():
    return

def button_click():
    return

def button_clear():
    return

def button_equal():
    return

#Definindo so botôes:
butt1 = Button(root, text="1",bg="Black",fg ="Green",padx=40,pady=20, command=button_click)
butt2 = Button(root, text="2",bg="Black",fg ="Green",padx=40,pady=20, command=button_click)
butt3 = Button(root, text="3",bg="Black",fg ="Green",padx=40,pady=20, command=button_click)
butt4 = Button(root, text="4",bg="Black",fg ="Green",padx=40,pady=20, command=button_click)
butt5 = Button(root, text="5",bg="Black",fg ="Green",padx=40,pady=20, command=button_click)
butt6 = Button(root, text="6",bg="Black",fg ="Green",padx=40,pady=20, command=button_click)
butt7 = Button(root, text="7",bg="Black",fg ="Green",padx=40,pady=20, command=button_click)
butt8 = Button(root, text="8",bg="Black",fg ="Green",padx=40,pady=20, command=button_click)
butt9 = Button(root, text="9",bg="Black",fg ="Green",padx=40,pady=20, command=button_click)
butt0 = Button(root, text="0",bg="Black",fg ="Green",padx=40,pady=20, command=button_click)
buttAdd = Button(root, text="+",bg="Black",fg ="Green",padx=39,pady=20, command=button_add)
buttClear = Button(root, text="Clear",bg="Black",fg ="Green",padx=79,pady=20, command=button_clear)
buttEqual = Button(root, text="=",bg="Black",fg ="Green",padx=91,pady=20, command=button_equal)


#Alocando os botôes no grid
butt0.grid(row=4, column=0)
buttClear.grid(row=4, column=1,columnspan=2)
buttEqual.grid(row=5, column=1,columnspan=2)
buttAdd.grid(row=5, column=0)

butt1.grid(row=3, column=0)
butt2.grid(row=3, column=1)
butt3.grid(row=3, column=2)

butt4.grid(row=2, column=0)
butt5.grid(row=2, column=1)
butt6.grid(row=2, column=2)

butt7.grid(row=1, column=0)
butt8.grid(row=1, column=1)
butt9.grid(row=1, column=2)

root.mainloop()