import tkinter as tk
from tkinter import ttk
from tkinter import *
import pymysql as sql
db = sql.connect(host="localhost", database="managingsystem", user="root", password="@123#")
c = db.cursor()
c.execute("select * from register")
r = c.fetchall()
tab=tk.Tk()
tab.geometry("600x300")
tab.maxsize(600,300)
tab.title("student registration")
listBox=ttk.Treeview(tab,selectmode='browse')
listBox.grid(row=20,column=20,rowspan=100,columnspan=100)  
listBox["columns"]=("Firstname","Lastname","Gender","Class","Fathername","rollno")
listBox["show"]='headings'
listBox.column("Firstname",width=100,anchor="c")
listBox.column("Lastname",width=100,anchor="c")
listBox.column("Gender",width=100,anchor="c")
listBox.column("Class",width=100,anchor="c")
listBox.column("Fathername",width=100,anchor="c")
listBox.column("rollno",width=100,anchor="c")

listBox.heading("Firstname",text="Firstname")
listBox.heading("Lastname",text="Lastname")
listBox.heading("Gender",text="Gender")
listBox.heading("Class",text="Class")
listBox.heading("Fathername",text="Fathername")
listBox.heading("rollno",text="RollNo")

def dl():
    tab.destroy()
    import delete
c = Button(tab, text="Delete", bg="black", fg="white", font=("arial", 13, "bold"),command=dl)
def back():
    tab.destroy()
    import ad

def update():
    tab.destroy()
    import ur


Button(tab,text="Update",bg="black",fg="white",font=("arial",13,"bold"),command=update).place(x=200,y=230)
d = Button(tab, text="back", bg="black", fg="white", font=("arial", 13, "bold"),command=back)
d.place(x=120,y=230)
c.place(x=30, y=230)


for x in r:
    listBox.insert("",'end',values=(x[0],x[1],x[2],x[3],x[4],x[5]))
tab.mainloop()
