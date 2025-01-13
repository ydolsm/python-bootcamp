import tkinter

# Create the main window
root = tkinter.Tk()

# Dropdown Menu
dropdown_var = tkinter.StringVar(value="Choice 1")
dropdown_menu = tkinter.OptionMenu(
    root, dropdown_var,
    "Choice 1",
    "Choice 2",
    "Choice 3")
dropdown_menu.pack()

# Run the application
root.mainloop()
