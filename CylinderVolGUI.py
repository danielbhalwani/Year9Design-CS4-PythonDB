import tkinter as tk

root = tk.Tk()
root.title("Volume of a Sphere")

labr = tk.Label(root, text= "radius")
labr.pack()

entr=tk.Entry(root)
entr.pack()


btn = tk.Button(root, text = "submit")
btn.pack()

output = tk.Text(root, width =50, height=10, borderwidth=3 relief=tk.GROOVE)
output.config(state="disabled")
output.pack()











root.mainloop()