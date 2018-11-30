import tkinter as tk 

root = tk.Tk () #Tk () is a special method called a constructor 
	# A constuctor is a special method only called once 
from datetime import datetime
import calendar
diff = 60 * 60 * 24
yesterday = datetime(*datetime.fromtimestamp(calendar.timegm(datetime.today().utctimetuple()) - diff).utctimetuple()[:3], hour=23, minute=30)
print (yesterday)

root.title('WorkTimeTrackerV1')
#Here is just the title of the program window
#********************************************************************

lab = tk.Label(root, text = "Welcome to WorkTimeTracker!")
lab.config(font=("Times new roman", 44))
#Here is a master title of the whole window

# to pack an element using the grid geometry manager. We use 
# <object>.grid(<perameters>) 

lab.grid(row = 0, column = 0)
#---------------------------------------------------------------------
#In this "_" area is all of my text box configuration and grid
ent = tk.Entry(root)
ent.grid(row =1, column = 0)

ent = tk.Entry(root)
ent.grid(row = 2, column = 0)

ent = tk.Entry(root)
ent.grid(row = 3, column = 0)


#---------------------------------------------------------------------

btn = tk.Button(root, text = "ENTER!")
btn.grid(row = 4, column = 0)

output = tk.Text(root) 
output.configure(state = "disabled", bg = "red")
output.grid(row = 0, column = 1, rowspan = 3)


root.mainloop()
