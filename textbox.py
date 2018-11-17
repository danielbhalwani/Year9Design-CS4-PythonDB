from tkinter import *

root = Tk()

root.geometry("500x600")

def print_hello():
	print("Hello World!")
	return


btn1 = Button(root, text="Click me!", command=print_hello)
btn1.pack(side="top")

lbll = Label(root, text= "Label").pack()

eBox = Entry(root).pack()

mainloop()