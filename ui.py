import main

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title('Renter Vehicle')
root.minsize(width=1400,height=700)
root.maxsize(width=1400,height=700)

uitype=StringVar()
uimax_passenger=IntVar()
uiac=BooleanVar()
uisize=IntVar()
uimaxload=IntVar()
uiid=IntVar()


def destroy1():
    L1 = Label(root, text="")
    L1.grid(row=2,rowspan=20, column=6, columnspan=6)
    L1.config(width=80,height=60)

def btnadd():
    destroy1()
    global uitype,uimax_passenger,uiac,uisize,uimaxload
    user=[uitype.get(),uimax_passenger.get(),uiac.get(),uisize.get(),uimaxload.get()]
    if main.Add(user)==1:
        messagebox.showinfo(title="Success", message="Vehicle Added Successfully")
        c.current(0)
    else:
        messagebox.showwarning(title="Can't find", message="No Vehicle found")

def btnremove():
    destroy1()
    global uiid
    if main.Remove(uiid.get())==1:
        messagebox.showinfo(title="Success", message="Vehicle Removed Successfully")
    else:
        messagebox.showwarning(title="Can't find", message="No Vehicle found")

def btnassign():
    destroy1()
    global uitype,uimax_passenger,uiac,uisize,uimaxload
    user=[uitype.get(),uimax_passenger.get(),uiac.get(),uisize.get(),uimaxload.get()]
    if main.Assign(user)==1:
        messagebox.showinfo(title="Success", message="Vehicle Assigned Successfully")
        c.current(0)
    else:
        messagebox.showwarning(title="Can't find", message="No Vehicle found")
def btnrelease():
    destroy1()
    global uiid
    if main.Release(uiid.get())==1:
        messagebox.showinfo(title="Success", message="Vehicle Released Successfully")
    else:
        messagebox.showwarning(title="Can't find", message="No Vehicle found")
def btnavailable():
    destroy1()
    list=main.Available()
    if len(list)>0:
        Available()
        row=3
        for x in range(len(list)):
            coloumn = 6
            for y in range(len(list[x])):
                if y==3:
                    if list[x][y]==1:
                        L1 = Label(root, text="True")
                        L1.config(font=('Arial', 12))  # change font
                        L1.config(fg='#000000')  # foreground
                        L1.config(height=1)
                        L1.grid(row=row, column=coloumn)
                    else:
                        L1 = Label(root, text="False")
                        L1.config(font=('Arial', 12))  # change font
                        L1.config(fg='#000000')  # foreground
                        L1.config(height=1)
                        L1.grid(row=row, column=coloumn)
                else:
                    L1 = Label(root, text=list[x] [y])
                    L1.config(font=('Arial', 12))  # change font
                    L1.config(fg='#000000')  # foreground
                    L1.config(height=1)
                    L1.grid(row=row, column=coloumn)
                coloumn+=1
            row+=1


    else:
        messagebox.showwarning(title="Can't find", message="No Vehicle Available in this movement")

L1 = Label(root, text="Cab Service")
L1.config(font=('Ink Free', 32))  # change font
L1.config(fg='#3268a8')  # foreground
L1.config(height=1)
L1.grid(row=0, columnspan=12)

L1 = Label(root, text="")
L1.grid(row=1,columnspan=6)
L1.config(height=3)
L1 = Label(root, text="Type")
L1.config(font=('Arial', 12))  # change font
L1.config(fg='#000000')  # foreground
L1.config(height=3)
L1.grid(row=2, column=0)
c = ttk.Combobox(root,textvariable=uitype, values=["","Car", "Van", "3wheelers","Truck", "Lorry"])
c.grid(row=2, column=1, pady=20)
c.current(0)
c.config(width=25)
L1 = Label(root, text="")
L1.grid(row=1,column=2)
L1.config(width=15)
L1 = Label(root, text="ID")
L1.config(font=('Arial', 12))  # change font
L1.config(fg='#000000')  # foreground
L1.config(height=3)
L1.grid(row=3, column=3)
E = Entry(root,textvariable=uiid, bd=2)
E.config(width=25)
E.insert(0, '')
E.grid(row=3, column=4)

B1 = Button(root, text="Release Vehicle", command=btnrelease)
B1.config(fg='#000000')  # foreground
B1.config(bg='#3268a8')  # background
B1.grid(row=4, column=4)
B1.config(width=15)
B1.config(height=2)

B1 = Button(root, text="Remove Vehicle", command=btnremove)
B1.config(fg='#000000')  # foreground
B1.config(bg='#3268a8')  # background
B1.grid(row=5, column=4)
B1.config(width=15)
B1.config(height=2)

L1 = Label(root, text="")
L1.grid(row=1,column=5)
L1.config(width=15)

def Available():
    L1 = Label(root, text="ID")
    L1.config(font=('Arial', 12))  # change font
    L1.config(fg='#000000')  # foreground
    L1.config(height=3,width=8)
    L1.grid(row=2, column=6)

    L1 = Label(root, text="Type")
    L1.config(font=('Arial', 12))  # change font
    L1.config(fg='#000000')  # foreground
    L1.config(height=3,width=10)
    L1.grid(row=2, column=7)

    L1 = Label(root, text="Max passenger")
    L1.config(font=('Arial', 12))  # change font
    L1.config(fg='#000000')  # foreground
    L1.config(height=3,width=12)
    L1.grid(row=2, column=8)

    L1 = Label(root, text="AC")
    L1.config(font=('Arial', 12))  # change font
    L1.config(fg='#000000')  # foreground
    L1.config(height=3,width=10)
    L1.grid(row=2, column=9)

    L1 = Label(root, text="Size")
    L1.config(font=('Arial', 12))  # change font
    L1.config(fg='#000000')  # foreground
    L1.config(height=3,width=10)
    L1.grid(row=2, column=10)

    L1 = Label(root, text="Max load")
    L1.config(font=('Arial', 12))  # change font
    L1.config(fg='#000000')  # foreground
    L1.config(height=3,width=10)
    L1.grid(row=2, column=11)

B1 = Button(root, text="Available Vehicle", command=btnavailable)
B1.config(fg='#000000')  # foreground
B1.config(bg='#3268a8')  # background
B1.grid(row=1, column=6, columnspan=5)
B1.config(width=15)
B1.config(height=2)

def list(a,b,c,d):
    global uimax_passenger
    L2 = Label(root, text="Max passenger")
    L2.config(font=('Arial', 12))  # change font
    L2.config(fg='#000000')  # foreground
    L2.config(height=3)
    L2.grid(row=3, column=0)
    c2 = ttk.Combobox(root, textvariable=uimax_passenger, values=a)
    c2.grid(row=3, column=1, pady=20)
    c2.current(0)
    c2.config(width=25)

    global uiac
    L2 = Label(root, text="AC(true/false)")
    L2.config(font=('Arial', 12))  # change font
    L2.config(fg='#000000')  # foreground
    L2.config(height=3)
    L2.grid(row=4, column=0)
    c3 = ttk.Combobox(root, textvariable=uiac, values=b)
    c3.grid(row=4, column=1, pady=20)
    c3.current(0)
    c3.config(width=25)

    global uisize
    L2= Label(root, text="Size")
    L2.config(font=('Arial', 12))  # change font
    L2.config(fg='#000000')  # foreground
    L2.config(height=3)
    L2.grid(row=5, column=0)
    c4= ttk.Combobox(root, textvariable=uisize, values=c)
    c4.grid(row=5, column=1, pady=20)
    c4.current(0)
    c4.config(width=25)

    global uimaxload
    L2 = Label(root, text="Max load")
    L2.config(font=('Arial', 12))  # change font
    L2.config(fg='#000000')  # foreground
    L2.config(height=3)
    L2.grid(row=6, column=0)
    c5= ttk.Combobox(root, textvariable=uimaxload, values=d)
    c5.grid(row=6, column=1, pady=20)
    c5.current(0)
    c5.config(width=25)

    B2 = Button(root, text="Add Vehicle", command=btnadd)
    B2.config(fg='#000000')  # foreground
    B2.config(bg='#3268a8')  # background
    B2.grid(row=7, column=0)
    B2.config(width=15)
    B2.config(height=2)

    B2 = Button(root, text="Assign Vehicle", command=btnassign)
    B2.config(fg='#000000')  # foreground
    B2.config(bg='#3268a8')  # background
    B2.grid(row=7, column=1)
    B2.config(width=15)
    B2.config(height=2)

def destroy2():
    L1 = Label(root, text="")
    L1.grid(row=3,rowspan=8, column=0, columnspan=2)
    L1.config(width=50,height=40)


def on_type_change(index, value, op):
    if uitype.get()=="Car":
        destroy2()
        list([3,4],[True,False],[0],[0])
    elif uitype.get()=="Van":
        destroy2()
        list([6, 8], [True, False], [0], [0])
    elif uitype.get()=="3wheelers":
        destroy2()
        list([3], [False],[0],[0])
    elif uitype.get()=="Truck":
        destroy2()
        list([0], [False], [7, 12],[0])
    elif uitype.get()=="Lorry":
        destroy2()
        list( [0],[False],[0],[2500, 3500])
    else:
        destroy2()


uitype.trace('w', on_type_change)





root.mainloop()