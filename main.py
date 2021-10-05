from tkinter import *
from PIL import Image, ImageTk

class admin__complete:
    def __init__(self, admin):
        self.admin=admin
        self.admin.geometry("1500x700")
        #heading
        heading = Label(self.admin, text="Student Management System", border=10,  bg="black", fg="white", font=("times new roman", 30, "bold"))
        heading.pack(fill=X)
        #Sections

        self.image = Image.open("adm2.jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        b = Label(image=self.photo)
        b.place(x=0, y=66)
        c = Button(admin, text="Admin", bg="black", fg="white", font=("arial", 13, "bold"))
        c.place(x=130, y=245)
        self.admin.title("Student management system")
        self.i = Image.open("u.jpg")
        self.p = ImageTk.PhotoImage(self.i)
        d = Label(image=self.p)
        d.place(x=1090, y=66)
        # user

        self.e = Image.open("red.jpg")
        self.f = ImageTk.PhotoImage(self.e)
        g = Label(image=self.f)
        g.place(x=450, y=320)

        def adminstrat():
            admin.destroy()
            import ad

        c = Button(admin, text="Admin", bg="black", fg="white", font=("arial", 13, "bold"),command=adminstrat)
        c.place(x=130, y=245)

        def registera():
            admin.destroy()
            import registrat

        # registration

        h = Button(admin, text="Registration", font=("arial", 13, "bold"), bg="black", fg="white",command=registera)
        h.place(x=640, y=600)

        def user():
            admin.destroy()
            import user

        e = Button(admin, text="User", bg="black", fg="white", font=("arial", 13, "bold"),command=user)
        e.place(x=1200, y=245)


admin=Tk()
b = admin__complete(admin)
admin.mainloop()

