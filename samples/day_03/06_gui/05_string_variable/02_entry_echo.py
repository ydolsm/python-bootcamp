import tkinter

# Create the main window
root = tkinter.Tk()

# Create an entry field
entry = tkinter.Entry(root)
entry.pack()

# Create a label
user_input = tkinter.StringVar(root, value="Hello")
label = tkinter.Label(textvariable=user_input)
label.pack()

# Function triggered on keypress
def display(event):
    user_input.set(entry.get())

# Bind key to Return key
entry.bind("<Return>", display)

# Run the application
root.mainloop()
