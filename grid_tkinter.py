from tkinter import *
from PIL import ImageTk, Image
# Program for partial screenshot 
import pyscreenshot , os,random

f = open("counter.txt",'r')
x = f.read()
x = int(x)
print(x)


WIN = Tk()
WIN.geometry("399x459+300+10")

Button_Frame = Frame(WIN,width=399,height=100)
Button_Frame.pack()

Main = Frame(WIN,width=399,height=399)
Main.pack()


o_list = os.listdir("O's")
x_list = os.listdir("X's")
O = random.choice(o_list)
X = random.choice(x_list)

img1 = Image.open("O's/"+O)
img1 = img1.resize((57, 57), Image.ANTIALIAS) 
photo1 = ImageTk.PhotoImage(img1) 

img2 = Image.open("X's/"+X)
img2 = img2.resize((57, 57), Image.ANTIALIAS) 
photo2 = ImageTk.PhotoImage(img2) 

img3 = Image.open("clear.png")
img3 = img3.resize((57, 57), Image.ANTIALIAS) 
clearimg = ImageTk.PhotoImage(img3) 

button_list = []

for i in range(49):
    f1 = Frame(Main,width=57,height=57,bg="black")
    b = Button(f1, text = "",borderwidth=4,bg="white")
    button_list.append(b)

    def left(event):
    	event.widget.config(image=photo1)
    def right(event):   
    	event.widget.config(image=photo2) 
    def clear(event):
        event.widget.config(image=clearimg)
        event.widget.image = clearimg

    b.bind("<Button-1>",left)
    b.bind("<Button-3>",right)
    b.bind('<Double-Button-1>', clear)
    f1.rowconfigure(0, weight = 1)
    f1.columnconfigure(0, weight = 1)
    f1.grid_propagate(0)
    f1.grid(row = i//7, column = i%7)


   # b.bind("<Button-1>",lambda k=i:first(k))
    b.grid(sticky = "NWSE")

# im=pyscreenshot.grab(bbox=(x1,x2,y1,y2)) 
def take():
        global x
        image = pyscreenshot.grab(bbox=(306,60,706,465))
        image.save(f"D:/Pygame_projects/7x7_CNN/images_for_Tie/TIE/img{x}.png")
        x += 1
        f = open("counter.txt",'w')
        f.write(str(x))

take = Button(Button_Frame,text="take",command=take)
take.pack(ipadx=15)


WIN.mainloop()
