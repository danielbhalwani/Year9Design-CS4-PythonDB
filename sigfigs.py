import tkinter as tk
import os as os



def change(*args):
	print("running change")
	print(var.get())

def setting():
	print("TEST")

def acc_press(event):
	acc_pressed = true

def acc_rel(event):
	acc_pressed = false

def submit():
	print("Submit pressed")
	output.insert(tk.END,"Paul")
	if varCheck.get() == 1:
		text = "You entered "+entIn1.get+ " the result is "+output.get()
		os.system("say "+text)


def checkchange():
	print(varCheck.get())

root = tk.Tk() 



OPTIONS = [
	"Sig Figs",
	"Micrometer conversion to centimeters",
]
var = tk.StringVar(root)
var.set(OPTIONS[0])
var.trace("w",change)
dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1])
dropDownMenu.pack()


varCheck = tk.IntVar(root)
checkAccess = tk.Checkbutton(root,text = "Accessibility", var = varCheck, command = checkchange)
checkAccess.pack()

labIn1 = tk.Label(root, text = "Input the number to operate on") 
labIn1.pack()

entIn1 = tk.Entry(root)
entIn1.pack(padx = 10)
binSubmit = tk.Button(root, text = "Submit", command = submit)
binSubmit.pack() 
output = tk.Entry(root)
output.config(state = "disable")
output.pack() 


root.mainloop() 