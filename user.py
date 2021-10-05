from tkinter import *
class login__here:
    def __init__(self,login):
        self.login= login
        self.login.geometry("500x500")
        self.login.maxsize(500,500)
        self.login.title("Login here")
        self.lig= StringVar()
        self.ps = StringVar()
        title = Label(self.login, text="Login", border=10,  bg="black", fg="white", font=("times new roman", 30, "bold"))
        title.pack(fill=X)
        l = Label(text="Username",font=("times new roman",15 , "bold"),fg="white", bg="black")
        l.place(x=50,y=100)
        p = Label(text="password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        p.place(x=50, y=150)
        le = Entry( width=10,textvariable=self.lig, font="arial 15")
        le.place(x=200,y=100)
        ld = Entry(width=10, textvariable=self.ps, font="arial 15",show="*")
        ld.place(x=200, y=150)

        def adminstrat():
            login.destroy()
            import main

        def dis():
            login.destroy()
            import table

        sub = Button(self.login, text="Submit", font=("arial", 15, "bold"), bg="black", fg="white",command=dis)
        sub.place(x=180, y=200)
        c = Button(login, text="back", bg="black", fg="white", font=("arial", 13, "bold"),command=adminstrat)
        c.place(x=200, y=250)
login = Tk()
d = login__here(login)

login.mainloop()




