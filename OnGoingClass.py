# Video at current time: 
from tkinter import *


root = Tk()
root.title('Calculadora Hypo')

entry = Entry(root, width=35,bg="Black",fg ="Green",borderwidth=15)
entry.grid(row=0, column=0, columnspan=3,padx=10,pady =10) #columnspan diz quantos espaços do grid tem que estender
#entry.insert(0,"") 


def button_add():
    return



butt1 = Button(root, text="1",bg="Black",fg ="Green",padx=40,pady=20, command=button_add)
butt1.grid(row=1, column=0)

butt2 = Button(root, text="2",bg="Black",fg ="Green",padx=40,pady=20, command=button_add)
butt2.grid(row=1, column=1)

butt3 = Button(root, text="3",bg="Black",fg ="Green",padx=40,pady=20, command=button_add)
butt3.grid(row=1, column=2)

butt4 = Button(root, text="4",bg="Black",fg ="Green",padx=40,pady=20, command=button_add)
butt4.grid(row=2, column=0)

butt5 = Button(root, text="5",bg="Black",fg ="Green",padx=40,pady=20, command=button_add)
butt5.grid(row=2, column=1)

butt6 = Button(root, text="6",bg="Black",fg ="Green",padx=40,pady=20, command=button_add)
butt6.grid(row=2, column=2)

butt7 = Button(root, text="7",bg="Black",fg ="Green",padx=40,pady=20, command=button_add)
butt7.grid(row=3, column=0)

butt8 = Button(root, text="8",bg="Black",fg ="Green",padx=40,pady=20, command=button_add)
butt8.grid(row=3, column=1)

butt9 = Button(root, text="9",bg="Black",fg ="Green",padx=40,pady=20, command=button_add)
butt9.grid(row=3, column=2)

butt0 = Button(root, text="0",bg="Black",fg ="Green",padx=40,pady=20, command=button_add)
butt0.grid(row=4, column=0)


root.mainloop()