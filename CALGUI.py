from tkinter import *
class Main_win(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master,bg="#2f3233")
        self.master=master
        self.cal()
    def cal(self):
        self.master.title("CALCULATOR")
        self.pack(fill=BOTH, expand=1)
        p = PhotoImage(file="/home/kar/icon.png")

        resized_photo = p.subsample(x=int(1900 / (167 * 3)),
                                    y=int(1900 / (167 * 3)))
        gg = Label(self, image=resized_photo,highlightthickness=0,borderwidth=False,activebackground="#68bfd5")
        gg.image = resized_photo
        gg.place(x=0, y=0)
        att={"highlightthickness":0,"borderwidth":False,"activebackground":"#68bfd5", "padx":20, "pady":2,"bg":"#363e40"}
        self.d=Entry(self,width=40,bg="#363e40",highlightthickness=0)
        self.d.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
        Button(self, text="1",highlightthickness=0,borderwidth=False,activebackground="#68bfd5", padx=20, pady=2,bg="#363e40", command= lambda :self.d.insert(len(str(self.d.get()))+1, "1")).grid(row=2, column=1,padx=10,pady=10)
        Button(self, text="2",highlightthickness=0,borderwidth=False,activebackground="#68bfd5",padx=20, pady=2,bg="#363e40",command= lambda :self.d.insert(len(str(self.d.get()))+1,"2")).grid(row=2, column=2,padx=10,pady=10)
        Button(self, text="3",padx=20,highlightthickness=0,borderwidth=False,activebackground="#68bfd5", pady=2,bg="#363e40",command= lambda :self.d.insert(len(str(self.d.get()))+1,"3")).grid(row=2, column=3,padx=10,pady=10)
        Button(self, text="+",padx=20,highlightthickness=0,borderwidth=False,activebackground="#68bfd5", pady=2,bg="#363e40",command= lambda :self.d.insert(len(str(self.d.get()))+1," + ")).grid(row=2, column=4,padx=10,pady=10)

        Button(self, text="4",padx=20,highlightthickness=0,borderwidth=False,activebackground="#68bfd5", pady=2,bg="#363e40",command= lambda :self.d.insert(len(str(self.d.get()))+1,"4")).grid(row=3, column=1,padx=10,pady=10)
        Button(self, text="5",padx=20,highlightthickness=0,borderwidth=False,activebackground="#68bfd5", pady=2,bg="#363e40",command= lambda :self.d.insert(len(str(self.d.get()))+1,"5")).grid(row=3, column=2,padx=10,pady=10)
        Button(self, text="6",padx=20,highlightthickness=0,borderwidth=False,activebackground="#68bfd5", pady=2,bg="#363e40",command= lambda :self.d.insert(len(str(self.d.get()))+1,"6")).grid(row=3, column=3,padx=10,pady=10)
        Button(self, text="-",padx=20,highlightthickness=0,borderwidth=False,activebackground="#68bfd5", pady=2,bg="#363e40",command= lambda :self.d.insert(len(str(self.d.get()))+1," - ")).grid(row=3, column=4,padx=10,pady=10)

        Button(self, text="7",padx=20,highlightthickness=0,borderwidth=False,activebackground="#68bfd5", pady=2,bg="#363e40",command= lambda :self.d.insert(len(str(self.d.get()))+1,"7")).grid(row=4, column=1,padx=10,pady=10)
        Button(self, text="8",padx=20,highlightthickness=0,borderwidth=False,activebackground="#68bfd5", pady=2,bg="#363e40",command= lambda :self.d.insert(len(str(self.d.get()))+1,"8")).grid(row=4, column=2,padx=10,pady=10)
        Button(self, text="9",padx=20,highlightthickness=0,borderwidth=False,activebackground="#68bfd5", pady=2,bg="#363e40",command= lambda :self.d.insert(len(str(self.d.get()))+1,"9")).grid(row=4, column=3,padx=10,pady=10)
        Button(self, text="*",padx=20,highlightthickness=0,borderwidth=False,activebackground="#68bfd5", pady=2,bg="#363e40",command= lambda :self.d.insert(len(str(self.d.get()))+1," * ")).grid(row=4, column=4,padx=10,pady=10)

        Button(self, text="0",padx=20,highlightthickness=0,borderwidth=False,activebackground="#68bfd5", pady=2,bg="#363e40",command= lambda :self.d.insert(len(str(self.d.get()))+1,"0")).grid(row=5, column=2,padx=10,pady=10)
        Button(self, text="/",padx=20,highlightthickness=0,borderwidth=False,activebackground="#68bfd5", pady=2,bg="#363e40",command= lambda :self.d.insert(len(str(self.d.get()))+1," / ")).grid(row=5, column=4,padx=10,pady=10)
        Button(self, text="%",padx=20,highlightthickness=0,borderwidth=False,activebackground="#68bfd5", pady=2,bg="#363e40",command= lambda :self.d.insert(len(str(self.d.get()))+1," % ")).grid(row=5, column=1,padx=10,pady=10)
        Button(self, text="^",padx=20,highlightthickness=0,borderwidth=False,activebackground="#68bfd5", pady=2,bg="#363e40",command= lambda :self.d.insert(len(str(self.d.get()))+1," ^ ")).grid(row=5, column=3,padx=10,pady=10)
        Button(self, text="C",padx=20,highlightthickness=0,borderwidth=False,activebackground="#68bfd5", pady=2,bg="#363e40",command= lambda :self.d.delete(first=0,last=len(str(self.d.get())))).grid(row=6,column=1,padx=10,pady=10)
        Button(self, text="del", padx=17,highlightthickness=0,borderwidth=False,activebackground="#68bfd5", pady=2,bg="#363e40", command=lambda: self.d.delete(first=len(str(self.d.get()))-1)).grid(row=6,column=2,padx=10,pady=10)
        Button(self, text="=",padx=60,highlightthickness=0,borderwidth=False,activebackground="#68bfd5", pady=2,bg="#363e40",command= lambda :self.ans()).grid(row=6, column=3,columnspan=2,padx=20,pady=10)
        self.e=Label(self, text="Result",bg="#363e40",highlightthickness=0,borderwidth=False,activebackground="#68bfd5",textvariable="op", padx=80)
        self.e.grid(row=7, column=1,columnspan=4,padx=10,pady=10)
    def ans(self):
        f=str(self.d.get())
        a=f.split(" ",3)
        if a[1] =="+":
            self.e.setvar("op",f"{int(a[0]) + int(a[2])}")
        elif a[1] =="-":
            self.e.setvar("op",f"{int(a[0]) - int(a[2])}")
        elif a[1] =="*":
            self.e.setvar("op",f"{int(a[0]) * int(a[2])}")
        elif a[1] =="/":
            self.e.setvar("op",f"{int(a[0]) / int(a[2])}")
        elif a[1] =="^":
            self.e.setvar("op",f"{int(a[0])**int(a[2])}")
        elif a[1] =="%":
            self.e.setvar("op",f"{int(a[0]) % int(a[2])}")


if __name__=="__main__":
    root=Tk()
    root.geometry("340x320")
    photo = PhotoImage(file="/home/kar/icon.png")
    root.iconphoto(True, photo)
    root.resizable(width=False, height=False)
    root=Main_win(root)
    root.mainloop()
