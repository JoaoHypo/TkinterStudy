from tkinter import *
import pandas as pd

root = Tk()

entry = Entry(root,width=50,bg="Black",fg ="Green",border=15)
entry.pack()
entry.insert(0,"Enter Your name") #Texo dentro da caixa!!


def myClick():
    hello = "Hello " + entry.get()
    mylabel = Label(root,text=hello)
    mylabel.pack()

MyButton = Button(root, text="Send it \n (〃￣︶￣)人(￣︶￣〃)", padx=50, pady=50,command=myClick, fg="pink",bg="green")
MyButton.pack()

root.mainloop()