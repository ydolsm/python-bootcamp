import tkinter

# Create the main window
root = tkinter.Tk()

# Create an entry field
entry = tkinter.Entry(root)
entry.pack()


# Function triggered on keypress
def print_input(event):
    user_input = entry.get()
    print(user_input)

# Bind key to Return key
entry.bind("<Return>", print_input)

# Run the application
root.mainloop()