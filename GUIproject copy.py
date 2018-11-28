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

#Add a section a code that highlights
#the appropriate section - Outfits, Pickaxes or Gliders
#************WIDGET 2,3,4 (Labels)**************
labInput1 = tk.Label(root, text = "Outfits")
labInput1.config(background = "black", foreground = "white")
labInput1.grid(row = 0, column = 0, sticky = "NESW")
labInput1.bind("<Button-1>",clicked1)

labInput2 = tk.Label(root, text = "Pickaxes")
labInput2.config(background = "grey", foreground = "black")
labInput2.grid(row = 1, column = 0, sticky = "NESW")
labInput2.bind("<Button-1>",clicked2)

labInput3 = tk.Label(root, text = "Gliders")
labInput3.config(background = "grey", foreground = "black")
labInput3.grid(row = 2, column = 0, sticky = "NESW")
labInput3.bind("<Button-1>",clicked3)


labInput4 = tk.Label(root, text = "Total = ___", background = "light blue")
labInput4.grid(row = 3, column = 1)

labInput6 = tk.Label(root, text = "Uncommon Skins", background = "light green")
labInput6.grid(row = 5, column = 0)

labInput7 = tk.Label(root, text = "Rare Skins: "+str(outfitR), background = "blue", foreground = "white")
labInput7.grid(row = 6, column = 0,  sticky = "NESW")

labInput8 = tk.Label(root, text = "___Epic Skins____", background = "purple")
labInput8.grid(row = 7, column = 0)

labInput9 = tk.Label(root, text = "Legendary Skins", background = "Gold")
labInput9.grid(row = 8, column = 0)

labInput10 = tk.Label(root, text = "Total = ____/100", background = "Green")
labInput10.grid(row = 8, column = 1)

root.mainloop() #Starts the program

