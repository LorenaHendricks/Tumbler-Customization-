import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Tumbler Customization Express!")

frame = Frame(window)
frame.pack()
bottomframe = Frame(window)
bottomframe.pack( side = BOTTOM )
pinkbutton = Button(frame, text = 'Pink', fg ='pink')
pinkbutton.pack( side = LEFT)
purplebutton = Button(frame, text = 'Purple', fg='purple')
purplebutton.pack( side = LEFT )
bluebutton = Button(frame, text ='Blue', fg ='blue')
bluebutton.pack( side = LEFT )

master = Tk()
master.title("First and Last name for shipping")
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

master = Tk()
master.title("What size would you like?")

var1 = IntVar()
Checkbutton(master, text='Small', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='Medium', variable=var2).grid(row=1, sticky=W)
var3 = IntVar()
Checkbutton(master, text='Large', variable=var3).grid(row=2, sticky=W)

frame1 = tk.Frame(master=window, width=300, height=300, bg="pink")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=250, bg="purple")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=200, bg="skyblue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"

def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"

window = tk.Tk()
window.title("How many tumblers would you like?")

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text="Take Away", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="Add More", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()