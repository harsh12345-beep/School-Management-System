from tkinter import *
from PIL import Image, ImageTk



i=Tk()
i.title("Options")
i.geometry("1100x600")
i.maxsize(1100,600)

image=Image.open('teacher.jpg')
photo=ImageTk.PhotoImage(image)
b = Label(image=photo)
b.place(x=0, y=0)

def teacher():
    i.destroy()
    import teacher
def emp():
    i.destroy()
    import employee
Button(i,text="Teacher",font=("times new roman", 20, "bold"),bg="black",fg="white",command=teacher).place(x=60,y=180)
imag=Image.open('employe.jpg')
phot=ImageTk.PhotoImage(imag)
c= Label(image=phot)
c.place(x=400, y=0)
Button(i,text="Employee",font=("times new roman", 20, "bold"),bg="black",fg="white",command=emp).place(x=450,y=195)
ima=Image.open('cancel.jpg')
pho=ImageTk.PhotoImage(ima)
d= Label(image=pho)
d.place(x=905, y=0)
def cancel():
    i.destroy()
    import main



Button(i,text="cancel",font=("times new roman", 20, "bold"),bg="black",fg="white",command=cancel).place(x=950,y=180)

i.mainloop()