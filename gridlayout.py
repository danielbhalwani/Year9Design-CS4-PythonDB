
import tkinter as tk

root = Tk()

Label(root, text="Red Sun", bg="red", fg="white").pack()
Label(root, text="Green Grass", bg="green", fg="black").pack()
Label(root, text="Blue Sky", bg="blue", fg="white").pack()

mainloop()

from Tkinter import *

root = Tk()

w = Label(root, text="Red Sun", bg="red", fg="white")
w.pack(fill=X)
w = Label(root, text="Green Grass", bg="green", fg="black")
w.pack(fill=X)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
w.pack(fill=X)

mainloop()