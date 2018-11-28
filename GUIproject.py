import tkinter as tk
#taking elements from tkinter
root = tk.Tk()
root.title('WorkTimeTracker V1')
labUN = tk.Label(root, text = "Hours")
#ordered parameters: The order we send them matters. (COMMON)
#named parameters: JavaScript and Python specifics

output = tk.Text(root,height = 30, width = 45) #Parameters
output.config(state = "disable", background = "antiquewhite")
output.grid(row = 0, column = 0, rowspan = 3, columnspan = 2)

output = tk.Text(root,height = 30, width = 45) #Parameters
output.config(state = "disable", background = "lightgreen")
output.grid(row = 0, column = 3, rowspan = 3, columnspan = 2)



output = tk.Text(root,height = 1, width = 16, borderwidth = 1, relief = "solid")
output.config(state = "normal")
output.grid(row = 0, column = 1)

output = tk.Text(root,height = 1, width = 16, borderwidth = 1, relief = "solid")
output.config(state = "normal")
output.grid(row = 1, column = 1)

output = tk.Text(root,height = 1, width = 16, borderwidth = 1, relief = "solid")
output.config(state = "normal")
output.grid(row = 2, column = 1)


labUN.pack()
entUN = tk.Entry(root)
entUN.pack(padx = 10)

labUN = tk.Label(root, text = "minutes")
labUN.pack()
entUN = tk.Entry(root)
entUN.pack(padx = 10)

labUN = tk.Label(root, text = "sites")
labUN.pack()
entUN = tk.Entry(root)
entUN.pack(padx = 10)

labUN = tk.Label(root, text = "Other side notes")
labUN.pack()
entUN = tk.Entry(root)
entUN.pack(padx = 10)

btnSubmit = tk.Button(root, text = "Confirm?")
btnSubmit.pack()

root.mainloop() #Starts the program

