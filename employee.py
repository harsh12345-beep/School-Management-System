import tkinter as tk
from tkinter import ttk
from tkinter import *
import pymysql as sql
db = sql.connect(host="localhost", database="managingsystem", user="root", password="kriti@123#")
c = db.cursor()
c.execute("select id,name,number,gender,experience,salary from employee")
r=c.fetchall()
tab=tk.Tk()
tab.geometry("600x300")
tab.maxsize(600,300)
tab.title("Employees in school")
listBox=ttk.Treeview(tab,selectmode='browse')
listBox.grid(row=20,column=20,rowspan=100,columnspan=100)
listBox["columns"]=("id","name","number","gender","experience","salary")
listBox["show"]='headings'
listBox.column("id",width=100,anchor="c")
listBox.column("name",width=100,anchor="c")
listBox.column("number",width=100,anchor="c")
listBox.column("gender",width=100,anchor="c")
listBox.column("experience",width=100,anchor="c")
listBox.column("salary",width=100,anchor="c")

listBox.heading("id",text="Id")
listBox.heading("name",text="Name")
listBox.heading("number",text="Phone number")
listBox.heading("gender",text="Gender")
listBox.heading("experience",text="Experience")
listBox.heading("salary",text="Salary")
def dl():
    tab.destroy()
    import dltemployee
def back():
    tab.destroy()
    import adlogafter
def up():
    tab.destroy()
    import uitemployee
def new():
    tab.destroy()
    import newteacher


Button(tab,text="New",bg="black",fg="white",font=("arial",13,"bold"),command=new).place(x=150,y=230)

Button(tab,text="Update",bg="black",fg="white",font=("arial",13,"bold"),command=up).place(x=350,y=230)
Button(tab,text="Back",bg="black",fg="white",font=("arial",13,"bold"),command=back).place(x=250,y=230)
c = Button(tab, text="Delete", bg="black", fg="white", font=("arial", 13, "bold"),command=dl)
c.place(x=30,y=230)


for x in r:
    listBox.insert("",'end',values=(x[0],x[1],x[2],x[3],x[4],x[5]))
tab.mainloop()