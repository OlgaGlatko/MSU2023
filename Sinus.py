from tkinter import *
from tkinter import messagebox
from math import *

def my_actionr():
    
    frm = int(e1.get())
    to   = int(e2.get())
    for i in range( frm, to):
        canvas.create_line(i,10*sin(i)+150, i+1, 10*sin(i)+150, fill='red', width=10)
def my_actionb():
    
    frm = int(e1.get())
    to   = int(e2.get())
    for i in range( frm, to):
        canvas.create_line(i,10*sin(i)+150, i+1, 10*sin(i)+150, fill='blue', width=10)
def my_actiong():
    
    frm = int(e1.get())
    to   = int(e2.get())
    for i in range( frm, to):
        canvas.create_line(i,10*sin(i)+150, i+1, 10*sin(i)+150, fill='green', width=10)

master = Tk()
master.title('Рисуем')

canvas = Canvas(master, width=800, height=400, background='black')
canvas.grid(column=0, row=1)

l1 = Label(master, text='t0')
l1.grid(row=2, column=0, sticky='e')
l2 = Label(master, text='t1')
l2.grid(row=3, column=0, sticky='e')

e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=2, column=1)
e2.grid(row=3, column=1)

b1 = Button(master, text="Draw red!", command = my_actionr)
b1.grid(row=4, column = 1)

b1 = Button(master, text="Draw blue!", command = my_actionb)
b1.grid(row=5, column = 1)

b1 = Button(master, text="Draw green!", command = my_actiong)
b1.grid(row=6, column = 1)



master.mainloop()