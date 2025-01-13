import tkinter

# Create the main window
root = tkinter.Tk()

# Create an entry field
entry = tkinter.Entry(root)
entry.pack()

# Create label component
text = tkinter.StringVar(root, value="")
label = tkinter.Label(textvariable=text)
label.pack()

def display():
    user_input = entry.get()
    text.set(user_input)

# Create a button
button = tkinter.Button(root, text="Submit", command=display)
button.pack()

# Run the application
root.mainloop()
