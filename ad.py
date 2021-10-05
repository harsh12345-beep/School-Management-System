from tkinter import *
from tkinter import Label


class login__here:
    def __init__(self, log):
        self.login = log
        self.login.geometry("500x500")
        self.login.maxsize(500, 500)
        self.login.title("Login here")
        self.First = StringVar()
        self.Last = StringVar()
        x = self.First.get()
        y = self.Last.get()
        title = Label(self.login, text="Login", border=10, bg="black", fg="white", font=("times new roman", 30, "bold"))
        title.pack(fill=X)
        l = Label(text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        l.place(x=50, y=100)
        p = Label(text="password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        p.place(x=50, y=150)
        le = Entry(width=10, textvariable=x, font="arial 15", )
        le.place(x=200, y=100)
        ld = Entry(width=10, textvariable=y, font="arial 15", show="*")
        ld.place(x=200, y=150)

        def adminstrat():
            log.destroy()
            import main

        def add():
            log.destroy()
            import adlogafter

        sub = Button(self.login, text="Submit", font=("arial", 15, "bold"), bg="black", fg="white", command=add)
        sub.place(x=180, y=200)

        c = Button(log, text="back", bg="black", fg="white", font=("arial", 13, "bold"), command=adminstrat)
        c.place(x=200, y=250)


login = Tk()
d = login__here(login)

login.mainloop()
