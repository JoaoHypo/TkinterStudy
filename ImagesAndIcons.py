from tkinter import *
#Tkinter nativamente só aceita .gif e .pnm
#Sendo assim precisamos importar algumas coisas do pacote Pillow, pacote de imagens do py
#Para lidar com formatos mais comuns como png e jpeg
from PIL import ImageTk,Image


root = Tk()
root.title('Images and Icons')
root.iconbitmap('D:\Python\TkinterStudy\iconteste.ico')

my_img = ImageTk.PhotoImage(Image.open('D:\Python\TkinterStudy\pngSample.png'))
my_img2 = ImageTk.PhotoImage(Image.open('D:\Python\TkinterStudy\JPEGsample.jpg'))


my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit Program", command=root.quit,image=my_img2)
button_quit.pack()

root.mainloop()