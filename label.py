from tkinter import *

def speak():
	print("hi")

main=Tk()
main.title("My GUI")
main.geometry("400x400")

Label(main, text="My button", width=12, command=speak).grid(row=1, column = 0, sticky=W)

main.mainloop()
