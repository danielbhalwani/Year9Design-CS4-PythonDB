import tkinter as tk 

root = tk.Tk ()

#Tk () is a special method called a constructor 
	# A constuctor is a special method only called once
root.config(background = "deepskyblue3")
#Every "variable" in python is limited to a certain scope. 
#The scope of a python "file" is the module-scope. ... The global keyword is the 
#way that you tell python that a particular variable in your function is defined 
#at the global (module-level) scope.
def datashowup():
	global site
	global hours
	global minutes
	global observations

	text.delete('1.0', tk.END)
	print("Wrapping into data summary...")
	site = ent3.get()
	hours = variable.get()
	minutes = var.get()
	observations = ent4.get()

	text.insert(tk.INSERT, site)
	text.insert(tk.INSERT, '\n' + hours + " hour(s)")
	text.insert(tk.INSERT, ", " + minutes + " minute(s)")
	text.insert(tk.INSERT, '\n Observations: ' + observations ) 

	

def submit():
	global site
	global hours
	global minutes
	global observations

	f = open('data.txt', "w")
	f.write(site + "," + hours + "," + minutes + "," + observations + ",")
	print("Data submitted...")

def submit2():
	text.delete('1.0', tk.END)
	f = open('data.txt', 'r')
	content = f.read()
	content = content.split(",")
	print(content)
	print("Retrieving last periods data...")
	text.insert(tk.INSERT, content[0])
	text.insert(tk.INSERT, "\n")
	text.insert(tk.INSERT, content[1])
	text.insert(tk.INSERT, "\n")
	text.insert(tk.INSERT, content[2])
	text.insert(tk.INSERT, "\n")
	text.insert(tk.INSERT, content[3])

def change(*args):
	print("hours")
	print(var.get())


def minutes(*args):
	print("minutes")
	print(var.get())

 #Tk () is a special method called a constructor 
	# A constuctor is a special method only called once 
from datetime import datetime
import calendar
diff = 60 * 60 * 24
yesterday = datetime(*datetime.fromtimestamp(calendar.timegm(datetime.today().utctimetuple()) - diff).utctimetuple()[:3], hour=23, minute=30)
print (yesterday)

root.title('WorkTimeTrackerV1')
#Here is just the title of the program window
#********************************************************************

lab = tk.Label(root, text = "Welcome to WorkTimeTracker!", background = "Royalblue2")
lab.config(font=("Verdana",45))
lab.grid(row = 0, column = 2, columnspan = 4, sticky="W,E")
#Here is a master title of the whole window

# to pack an element using the grid geometry manager. We use 
# <object>.grid(<perameters>) 

lab.grid(row = 0, column = 0)
#---------------------------------------------------------------------
#In this "_" area is all of my text box configuration and grid
ent1 = tk.Entry(root, background = "Royalblue2")
ent1.grid(row = 5, column = 0,)
ent2 = tk.Entry(root, background = "Royalblue2")
ent2.grid(row = 5, column = 1,)
ent3 = tk.Entry(root, background = "Royalblue2")
ent3.grid(row = 5, column = 2,)
ent4 = tk.Entry(root,background = "Royalblue2")
ent4.grid(row = 5, column = 3,)

#---------------------------------------------------------------------
#This area is where the entry box labels will be
lab1 = tk.Label(root, text = "Hours" , background = "white")
lab1.grid(row = 4, column = 0)
lab1.config(font=("Verdana",27))

lab2 = tk.Label(root, text = "Minutes" , background = "white")
lab2.grid(row = 4, column = 1)
lab2.config(font=("Verdana",27))

lab3 = tk.Label(root, text = "Site" , background = "white")
lab3.grid(row = 4, column = 2)
lab3.config(font=("Verdana",27))

lab4 = tk.Label(root, text = "Observations" , background = "white")
lab4.grid(row = 4, column = 3)
lab4.config(font=("Verdana",27))

btn = tk.Button(root, text = "Submit!", background = "blue4",command = submit)
btn.grid(row = 11, column =3,sticky="W,E" )
btn.config(font=("Verdana", 25, "bold"))

btn = tk.Button(root, text = "Last Periods Data", background = "blue4",command = submit2)
btn.grid(row = 11, column =0,sticky="W" )
btn.config(font=("Verdana", 25, "bold"))

btn = tk.Button(root, text = "View data summary in above area", background = "blue4",command = datashowup)
btn.grid(row = 11, column =1, columnspan = 2,sticky="W" )
btn.config(font=("Verdana", 25 , "bold"))

#output = tk.Text(root) 
#output.grid(row = 0, column = 0, rowspan = 1)
#----------------------------------------------------------------------
#here are is the display box for data summaary

#w = ent1.get()
#x = ent2.get()
#y = ent3.get()
#z = ent4.get()

#text = tk.Text(root, background = "black", foreground = "white",height = 10, width = 65)
#text.insert("1.0", w+"/n"+x)																
#text.grid(row = 9, column = 0, columnspan = 4, sticky = "W,E")

#tk.ent1.get()

text = tk.Text(root, background = "black", foreground = "white", height = 10, width = 65)


text.grid(row = 9, column = 0, columnspan = 4, sticky = "W,E")

#Here are the arrow key selections for the times
#----------------------------------------------------------------------
OPTIONS = [
	"10",
	"20",
	"30",
	"40",
	"50",
	"55",
]
var = tk.StringVar(root)
var.set(OPTIONS[0])
var.trace("w",minutes)
dropDownMenu = tk.OptionMenu(root,var, OPTIONS[0],OPTIONS[1], OPTIONS[2], OPTIONS[3],OPTIONS[4],OPTIONS[5])
dropDownMenu.grid(row = 5, column =1)
dropDownMenu.grid()

OPTIONS = [
	"1",
	"2",
	"3",
	"4",
	"5",
	"6",
	"7",
	"8",
	"9",
]
variable = tk.StringVar(root)
variable.set(OPTIONS[0])
variable.trace("w",change)
dropDownMenu1 = tk.OptionMenu(root,variable, OPTIONS[0],OPTIONS[1], OPTIONS[2], OPTIONS[3],OPTIONS[4],OPTIONS[5],OPTIONS[6],OPTIONS[7],OPTIONS[8])
dropDownMenu1.grid(row = 5, column =0)
dropDownMenu1.grid()



root.mainloop()
