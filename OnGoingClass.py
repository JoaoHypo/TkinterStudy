from tkinter import *
#Tkinter nativamente só aceita .gif e .pnm
#Sendo assim precisamos importar algumas coisas do pacote Pillow, pacote de imagens do py
#Para lidar com formatos mais comuns como png e jpeg
from PIL import ImageTk,Image


root = Tk()
root.title('Images and Icons')
root.iconbitmap('D:\Python\TkinterStudy\ImgNIcons\iconteste.ico')








root.mainloop()