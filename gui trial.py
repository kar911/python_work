from tkinter import *
root=Tk()
root.geometry("1600x900")
btn=Button(root,text='dasdsad',command=root.destroy)
btn.place(x=50,y=100)
root.mainloop()
class winmian(Frame):
def __init__(self,master=None):
    Frame.__init__(self,master)
    self.master=master
    self.init_window()
def init_window(self):
    self.master.title("practice")
    self.pack(fill=BOTH,expand=1)
    enty=Entry(self,font=5)
    enty.place(x=100,y=100)
    Button(self,text="happy now",command=lambda :self.cal(enty.get())).place(x=0, y=0)
def cal(self,e):
    Label(self,text=e).place(x=50,y=50)
if __name__=="__main__":
root=Tk()
root.geometry("500x500")
root=winmian(root)
root.mainloop()
import sys
from tkinter import *
from tkinter import ttk
import time
from datetime import datetime
now= datetime.now()

d = dict()
def quit():
    print("Have a great day! Goodbye :)")
    sys.exit(0) 
def display():
    print(str(d))
def add(*args):
    global stock
    global d
    stock = stock_Entry.get()
    Quantity = Quantity_Entry.get()
    if stock not in d:
        d[stock] = Quantity
    else:
        d[stock] += Quantity




root = Tk()
root.title("Homework 5 216020088")

mainframe = ttk.Frame(root, padding="6 6 20 20")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

d=ttk.Label(mainframe, text="you are accesing this on day %s of month %s of %s" % (now.day,now.month,now.year)+" at exactly %s:%s:%s" % (now.hour,now.minute,now.second), foreground="yellow", background="Black")
d.grid(column=0, row = 0)

stock_Entry= ttk.Entry(mainframe, width = 60, textvariable="stock")
stock_Entry.grid(column=0, row = 1, sticky=W)
ttk.Label(mainframe, text="Please enter the stock name").grid(column=1, row = 1, sticky=(N, W, E, S))

Quantity_Entry= ttk.Entry(mainframe, width = 60, textvariable="Quantity")
Quantity_Entry.grid(column=0, row = 2, sticky=W)
ttk.Label(mainframe, text="Please enter the quantity").grid(column=1, row = 2, sticky=(N, W, E, S))

ttk.Button(mainframe, text="Add", command=add).grid(column=0, row=3, sticky=W)
ttk.Button(mainframe, text="Display", command=display).grid(column=0, row=3, sticky=S)
ttk.Button(mainframe, text="Exit", command=quit).grid(column=0, row=3, sticky=E)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.mainloop()
