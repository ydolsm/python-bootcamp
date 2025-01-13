import tkinter

def print_left(event):
    print("Left")

# Create the main window
root = tkinter.Tk()

# Create an entry field
entry = tkinter.Entry(root)
entry.pack()

root.bind("<Left>", print_left)

# Run the application
root.mainloop()
