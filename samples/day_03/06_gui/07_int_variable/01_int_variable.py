import tkinter

# Create the main window
root = tkinter.Tk()

# Create a label with dynamic text
count = tkinter.IntVar(root, value=0)
label = tkinter.Label(root, textvariable=count)
label.pack()

def increment():
	count.set(count.get() + 1)

# Create a button
button = tkinter.Button(root, text=" + ", command=increment)
button.pack()

# Run the application
root.mainloop()
