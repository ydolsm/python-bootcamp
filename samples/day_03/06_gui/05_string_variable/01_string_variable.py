import tkinter

# Create the main window
root = tkinter.Tk()

# Create a label
text = tkinter.StringVar(root, value="Hello")
label = tkinter.Label(root, textvariable=text)
label.pack()

# Run the application
root.mainloop()