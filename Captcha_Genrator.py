from io import BytesIO
from tkinter import *
from random import *
from tkinter import messagebox
import string
from captcha.image import ImageCaptcha

image = ImageCaptcha(fonts=['G:/CAPTCHA-GENERATOR/fonts/ChelseaMarketsr.ttf', 'G:/CAPTCHA-GENERATOR/fonts/DejaVuSanssr.ttf'])

random=str(randint(100000, 999999))
data = image.generate(random)
assert isinstance(data, BytesIO)
image.write(random, 'out.png')

def verify():
    global random
    x=t1.get("0.0",END)
    if(int(x)==int(random)):
        messagebox.showinfo("Mission_complete", "Dang sorry Bro I though you were AI")
    else:
        messagebox.showinfo("MissionFailedSir", "Bro it happens dont worry Always TRY AGAIN")
        refresh()

def refresh():
    random=str(randint(100000, 999999))
    data = image.generate(random)
    assert isinstance(data, BytesIO)
    image.write(random,'out.png')
    l1.config(image=photo,height=100,width=200)
    l1.update()
    UpdateLabel()

def UpdateLabel():
    photo = PhotoImage(file="out.png")
    l1.config(image=photo, height=100, width=200)
    l1.image = photo  # Keep a reference to avoid garbage collection
    l1.update()

root=Tk()
photo = PhotoImage(file="out.png")

l1=Label(root,image=photo,height=200,width=400)
t1=Text(root,height=10,width=100)
b1=Button(root,text="submity",command=verify)
b2=Button(root,text="refreshy",command=refresh)

l1.pack()
t1.pack()
b1.pack()
b2.pack()
root.mainloop()


