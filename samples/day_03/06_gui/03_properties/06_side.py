import tkinter

# Create the main window
root = tkinter.Tk()

# Create a label
"""
Options: 
     "n", "ne", "e", "se", "s", "sw", "w", "nw", "center"
"""
label = tkinter.Label(root, text="Hello!", anchor='e', width=300)
label.pack()

# Run the application
root.mainloop()
