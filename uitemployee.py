from tkinter import *
from tkinter import Label

new = Tk()
new.geometry("900x900")
new.title("update in Employee")
Id = IntVar()
name = StringVar()
number = IntVar()
Gender = StringVar()
experience = StringVar()
salary = StringVar()


def newst():
    import pymysql as sql
    F = Id.get()
    F1 = name.get()
    F2 = number.get()
    F3 = Gender.get()
    F4 = experience.get()
    F5 = salary.get()
    db = sql.connect(host="localhost", password="@123#", user="root", database="managingsystem")
    D = db.cursor()
    sql = "update employee set name='%s',number='%s',gender='%s',experience='%s',salary='%s' where id='%s'" % (F1, F2, F3, F4, F5, F)
    D.execute(sql)
    db.commit()
    db.close()


heading = Label(new, text="Updatation In Table Using Id", border=10, bg="black", fg="white",
                font=("times new roman", 30, "bold"))
heading.pack(fill=X)
a = Label(text="Id", font="arial 15", bd=10, bg="black", fg="white")
a.place(x=50, y=130)
le = Entry(width=10, textvariable=Id, font="arial 15")
le.place(x=200, y=130)
b = Label(new, text="Name", font="arial 15", bd=10, bg="black", fg="white")
b.place(x=50, y=200)
le = Entry(width=10, textvariable=name, font="arial 15")
le.place(x=200, y=200)
c = Label(new, text="Number", font="arial 15", bd=10, bg="black", fg="white")
c.place(x=50, y=270)
le = Entry(width=10, textvariable=number, font="arial 15")
le.place(x=200, y=270)
d = Label(new, text="Gender", font="arial 15", bd=10, bg="black", fg="white")
d.place(x=50, y=340)
le = Entry(width=10, textvariable=Gender, font="arial 15")
le.place(x=200, y=340)
e = Label(new, text="Experience", font="arial 15", bd=10, bg="black", fg="white")
e.place(x=50, y=410)
le = Entry(width=10, textvariable=experience, font="arial 15")
le.place(x=200, y=410)
e = Label(new, text="Salary", font="arial 15", bd=10, bg="black", fg="white")
e.place(x=50, y=480)
pe = Entry(width=10, textvariable=salary, font="arial 15")
pe.place(x=200, y=480)
c = Button(new, text="Submit", bg="black", fg="white", font=("arial", 13, "bold"), command=newst)
c.place(x=150, y=550)


def adminstrat():
    new.destroy()
    import employee


d = Button(new, text="back", bg="black", fg="white", font=("arial", 13, "bold"), command=adminstrat)
d.place(x=150, y=600)
new.mainloop()
