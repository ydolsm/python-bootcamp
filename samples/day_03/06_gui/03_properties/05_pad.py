import tkinter

# Create the main window
root = tkinter.Tk()

# Create the left label
label = tkinter.Label(root, text="Left")
label.pack(side="left")

# Create the right label
label = tkinter.Label(root, text="Right")
label.pack(side="right")

# Run the application
root.mainloop()
