import tkinter as tk
#taking elements from tkinter
root = tk.Tk()
root.title('WorkTimeTracker V1')
root.configure(bg='red')
labUN = tk.Label(root, text = "Hours")
#ordered parameters: The order we send them matters. (COMMON)
#named parameters: JavaScript and Python specifics
from datetime import datetime
import calendar
diff = 60 * 60 * 24
yesterday = datetime(*datetime.fromtimestamp(calendar.timegm(datetime.today().utctimetuple()) - diff).utctimetuple()[:3], hour=23, minute=30)
print (yesterday)



Label(root, text="red", bg="red", fg="white")
pack(padx=5, pady=10, side=LEFT)
Label(root, text="green", bg="green", fg="black")
Pack(padx=5, pady=20, side=LEFT)
Label(root, text="blue", bg="blue", fg="white")
Pack(padx=5, pady=20, side=LEFT)














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

btnSubmit = tk.Button(root, text = "Submit")
btnSubmit.pack()



root.mainloop() #Starts the program

