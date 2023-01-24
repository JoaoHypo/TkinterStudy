from tkinter import *

root = Tk()
root.title('Calculadora Hypo')

entry = Entry(root, width=35,bg="Black",fg ="Green",borderwidth=15)
entry.grid(row=0, column=0, columnspan=3,padx=10,pady =10) #columnspan diz quantos espaços do grid tem que estender
#entry.insert(0,"") 

def button_click(number):
    current = entry.get()
    entry.delete(0, END) #Deleta a caixa de entrada, do começo ao fim 0 index inicial, end, o fim
    entry.insert(0,str(current) + str(number)) #Adiciona ao index 0 o parametro number
    
def button_add():
    primeironum = entry.get()
    global primNum
    primNum = float(primeironum)
    entry.delete(0, END)
    global method
    method = '+'

def button_sub():
    primeironum = entry.get()
    global primNum
    primNum = float(primeironum)
    entry.delete(0, END)
    global method
    method = '-'

def button_div():
    primeironum = entry.get()
    global primNum
    primNum = float(primeironum)
    entry.delete(0, END)
    global method
    method = '/'

def button_multi():
    primeironum = entry.get()
    global primNum
    primNum = float(primeironum)
    entry.delete(0, END)
    global method
    method = '*'

def button_clear():
    entry.delete(0, END)
    
def button_equal():
    segundonum = (entry.get())
    if method == '+':
        equal = primNum + float(segundonum)
    elif method == '-':
        equal = primNum - float(segundonum)
    elif method == '/':
        equal = primNum / float(segundonum)
    elif method == '*':
        equal = primNum * float(segundonum)

    entry.delete(0, END)
    entry.insert(0,equal)

#Definindo so botôes:
butt1 = Button(root, text="1",bg="Black",fg ="Green",padx=40,pady=20, command= lambda: button_click(1)) #Lambda somente para passar arugemtos
butt2 = Button(root, text="2",bg="Black",fg ="Green",padx=40,pady=20, command= lambda: button_click(2))
butt3 = Button(root, text="3",bg="Black",fg ="Green",padx=40,pady=20, command= lambda: button_click(3))
butt4 = Button(root, text="4",bg="Black",fg ="Green",padx=40,pady=20, command= lambda: button_click(4))
butt5 = Button(root, text="5",bg="Black",fg ="Green",padx=40,pady=20, command= lambda: button_click(5))
butt6 = Button(root, text="6",bg="Black",fg ="Green",padx=40,pady=20, command= lambda: button_click(6))
butt7 = Button(root, text="7",bg="Black",fg ="Green",padx=40,pady=20, command= lambda: button_click(7))
butt8 = Button(root, text="8",bg="Black",fg ="Green",padx=40,pady=20, command= lambda: button_click(8))
butt9 = Button(root, text="9",bg="Black",fg ="Green",padx=40,pady=20, command= lambda: button_click(9))
butt0 = Button(root, text="0",bg="Black",fg ="Green",padx=40,pady=20, command= lambda: button_click(0))
buttAdd = Button(root, text="+",bg="orange",fg ="white",padx=40,pady=20, command= button_add)
buttSub = Button(root, text="-",bg="orange",fg ="white",padx=40,pady=20, command= button_sub)
buttDiv = Button(root, text="/",bg="orange",fg ="white",padx=40,pady=20, command= button_div)
buttMulti = Button(root, text="*",bg="orange",fg ="white",padx=40,pady=20, command= button_multi)
buttClear = Button(root, text="Clear",bg="Blue",fg ="white",padx=76,pady=20, command= button_clear)
buttEqual = Button(root, text="=",bg="Green",fg ="Black",padx=40,pady=50, command= button_equal)

#Alocando os botôes no grid
butt0.grid(row=4, column=0,columnspan=1)
buttClear.grid(row=4, column=1,columnspan=2)
buttEqual.grid(row=5, column=2,columnspan=1,rowspan=2)
buttAdd.grid(row=5, column=0,columnspan=1)
buttSub.grid(row=6, column=0,columnspan=1)
buttDiv.grid(row=5, column=1,columnspan=1)
buttMulti.grid(row=6, column=1,columnspan=1)

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