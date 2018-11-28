# IMporting tkinter bassicallly contains all the support
#material to makee GUi elements
#by including "as tk" we are giving a short name ot use
import tkinter as tk

#With the login page all elements are vertically aligned
# this would be an instance where just using pack would be ifne


#Main window
root = tk.Tk()
root.title('WorkTimeTracker V1')
 #creates the standard main window
#Tk() is a special function called a CONSTRUCTOR
#if a function is written with a capital letter it indicates
#that it is a constructr 
#root.title sets a title for the window. The title for my progeam is "WorkTimeTracker V1"

#W**************_____WIDGET 1_____*********************
#Three stages to build elements/objects
#1. CONSTRUCT the Object: We build and configure it.
#2. Configure the object: WE specify behaviours and  settings (OPTIONAL)
#3. Pack the Object: Put it in the window
labUN = tk.Label(root, text = "Username")
#ordered parameters: The order we send them matters. (COMMON)
#named parameters: JavaScript and Python specifics
labUN.pack()


entUN = tk.Entry(root)
entUN.pack(padx = 10)

btnSubmit = tk.Button(root, text = "Submit")
btnSubmit.pack()

#We are writing an EVENT DRIVE PROGRAM
#Build the GUI
#Start it running 
#Wait for "EVENT"
root.mainloop() #Starts the program