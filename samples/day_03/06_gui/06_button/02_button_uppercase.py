import tkinter

def on_button_click():
    user_input = entry.get()
    text.set(user_input.upper())

# Create the main window
root = tkinter.Tk()

# Create an entry field
entry = tkinter.Entry(root)
entry.pack()

# Create a button
button = tkinter.Button(root, text="Submit", command=on_button_click)
button.pack()

# Create label component
text = tkinter.StringVar(root, value="")
label = tkinter.Label(textvariable=text)
label.pack()

# Run the application
root.mainloop()
