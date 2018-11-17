
from tkinter import *
master = Tk()

def closewindow () :
	exit()

button = Button(master, text = "Close Window", command=closewindow)
button.pack()
mainloop()