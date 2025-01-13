import tkinter

# Create the main window
root = tkinter.Tk()

# Checkbox
check_value = tkinter.BooleanVar()
checkbox = tkinter.Checkbutton(root, text="Enable", variable=check_value)
checkbox.pack()

# Run the application
root.mainloop()