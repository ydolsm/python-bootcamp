import tkinter

# Create the main window
root = tkinter.Tk()

# Radio Buttons
radio_var = tkinter.StringVar(value="Option B")

radio1 = tkinter.Radiobutton(root, text="Option A", variable=radio_var, value="Option A")
radio2 = tkinter.Radiobutton(root, text="Option B", variable=radio_var, value="Option B")
radio3 = tkinter.Radiobutton(root, text="Option C", variable=radio_var, value="Option C")

radio1.pack()
radio2.pack()
radio3.pack()

# Run the application
root.mainloop()
