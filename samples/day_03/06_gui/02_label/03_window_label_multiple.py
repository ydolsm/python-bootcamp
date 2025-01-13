import tkinter

# Create the main window
root = tkinter.Tk()

message = """
    Hello World
    In Multiple Lines
"""

# Create a label
label = tkinter.Label(root, text=message)
label.pack()

# Run the application
root.mainloop()
