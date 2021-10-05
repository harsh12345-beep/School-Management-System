from tkinter import *
from tkinter import messagebox
t=Tk()
t.title("Id")
t.geometry("500x300")
t.maxsize(500,300)
x=StringVar()
def delete():
    import pymysql as sql
    z = x.get()
    db = sql.connect(host="localhost", password="kriti@123#", user="root", database="managingsystem")
    c = db.cursor()
    sql = "delete from employee where id=('%s')"%(z)
    c.execute(sql)
    db.commit()
    db.close()
    messagebox.showinfo("result","Data Deleted Successfuly")
def back():
    t.destroy()
    import adlogafter
Button(t,text="back",fg="white",bg="black",font=("arial",13,"bold"),command=back).place(x=250,y=170)

le = Entry( width=10,textvariable=x, font="arial 15")
le.place(x=250,y=105)
c = Button(t, text="Delete", bg="black", fg="white", font=("arial", 13, "bold"),command=delete)
c.place(x=150, y=170)
heading = Label(t, text="Deleting Data", border=10,  bg="black", fg="white", font=("times new roman", 30, "bold"))
heading.pack(fill=X)
a=Label(t,text="Id",bg="black",fg="white",font=("times new roman", 20))
a.place(x=80,y=100)
t.mainloop()