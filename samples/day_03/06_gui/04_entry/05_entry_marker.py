import tkinter
# Create the main window
root = tkinter.Tk()

# Create an entry field
entry = tkinter.Entry(root)
entry.pack()

# Function triggered on keypress
def show_input(event):
    user_input = entry.get()

    # Create new label
    new_label = tkinter.Label(text=user_input)
    new_label.pack()


# Bind key to Return key
entry.bind("<Return>", show_input)

# Run the application
root.mainloop()