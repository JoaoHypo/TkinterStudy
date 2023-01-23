from tkinter import *
#Tkinter nativamente só aceita .gif e .pnm
#Sendo assim precisamos importar algumas coisas do pacote Pillow, pacote de imagens do py
#Para lidar com formatos mais comuns como png e jpeg
from PIL import ImageTk,Image


root = Tk()
root.title('Images and Icons')
root.iconbitmap('D:\Python\TkinterStudy\ImgNIcons\iconteste.ico')

my_img1 = ImageTk.PhotoImage(Image.open('D:\Python\TkinterStudy\ImgNIcons\pngSample.png'))
my_img2 = ImageTk.PhotoImage(Image.open('D:\Python\TkinterStudy\ImgNIcons\JPEGsample.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('D:\Python\TkinterStudy\ImgNIcons\Teste1.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('D:\Python\TkinterStudy\ImgNIcons\Teste2.png'))

#Lista das imagens
image_list = (my_img1, my_img2, my_img3, my_img4)

#Plotando a primeira imagem
my_label = Label(image=my_img1)
my_label.grid(row=0, column=0,columnspan=3)

def forward(imageIndex):
    
    #Função para frente, torna global a atualização da imagem e dos botôes
    global my_label
    global back_button
    global foward_button
    
    my_label.grid_forget() #Limpa o Grid
    my_label = Label(image=image_list[imageIndex - 1])#Plota a imagem
    foward_button = Button(root,text=">>",command = lambda:forward(imageIndex+1)) #Ataualiza os botôes chamando as proximas images já
    back_button = Button(root,text="<<",command = lambda:back(imageIndex-1))

    if imageIndex == int(len(image_list)):
        foward_button = Button(root,text=">>",state=DISABLED)

    #Plota no grid os novos botôes
    my_label.grid(row=0, column=0,columnspan=3)
    foward_button.grid(row=1,column=2)
    back_button.grid(row=1,column=0)

def back(imageIndex):
    global my_label
    global back_button
    global foward_button

    my_label.grid_forget()
    my_label = Label(image=image_list[imageIndex - 1])
    foward_button = Button(root,text=">>",command = lambda:forward(imageIndex+1))
    back_button = Button(root,text="<<",command = lambda:back(imageIndex-1))

    if imageIndex == 1:
        back_button = Button(root,text="<<",state=DISABLED)

    my_label.grid(row=0, column=0,columnspan=3)
    foward_button.grid(row=1,column=2)
    back_button.grid(row=1,column=0)

#Botoões iniciais
back_button = Button(root,text="<<",state=DISABLED)
exit_button = Button(root,text="EXIT PROGRAM",command= root.quit)
foward_button = Button(root,text=">>",command = lambda:forward(2))

back_button.grid(row=1,column=0)
exit_button.grid(row=1,column=1)
foward_button.grid(row=1,column=2)

root.mainloop()