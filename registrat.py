from tkinter import *
from tkinter import messagebox
from tkinter import Label
new = Tk()
new.geometry("900x900")
new.title("New Student Registration")
First = StringVar()
Last = StringVar()
Class = IntVar()
Gender = StringVar()
Father = StringVar()

def newst():
    import pymysql as sql
    F = First.get()
    F1 = Last.get()
    F2 = Gender.get()
    F3 = Class.get()
    F4 = Father.get()
    db = sql.connect(host="localhost",password="@123#",user="root",database="managingsystem")
    c = db.cursor()
    sql="insert into register(Firstname,Lastname,Gendre,Class,Fathername) values('%s','%s','%s','%s','%s')"%(F, F1, F2, F3, F4)
    c.fetchall;
    c.execute(sql)
    db.commit()
    db.close()

heading = Label(new, text="Student Registration page", border=10,  bg="black", fg="white", font=("times new roman", 30, "bold"))
heading.pack(fill=X)
a= Label(text="First name",font="arial 15",bd=10,bg="black",fg="white")
a.place(x=50,y=130)
le = Entry( width=10,textvariable=First, font="arial 15")
le.place(x=200,y=130)
b = Label(new, text="Last name", font="arial 15",bd=10,bg="black",fg="white")
b.place(x=50,y=200)
le = Entry( width=10,textvariable=Last, font="arial 15")
le.place(x=200,y=200)
c = Label(new, text="Gender", font="arial 15",bd=10,bg="black",fg="white")
c.place(x=50,y=270)
le = Entry( width=10,textvariable=Gender, font="arial 15")
le.place(x=200,y=270)
d = Label(new, text="Class", font="arial 15",bd=10,bg="black",fg="white")
d.place(x=50,y=340)
le = Entry( width=10,textvariable=Class, font="arial 15")
le.place(x=200,y=340)
e = Label(new, text="Father", font="arial 15",bd=10,bg="black",fg="white")
e.place(x=50,y=410)
le = Entry( width=10,textvariable=Father, font="arial 15")
le.place(x=200,y=410)
def succes():
    messagebox.showinfo("Result","Registration Successful")
c = Button(new, text="Submit", bg="black", fg="white", font=("arial", 13, "bold"),command=newst)
c.place(x=150, y=500)
def adminstrat():
    new.destroy()
    import main
c = Button(new, text="back", bg="black", fg="white", font=("arial", 13, "bold"), command=adminstrat)
c.place(x=150, y=550)
new.mainloop()
