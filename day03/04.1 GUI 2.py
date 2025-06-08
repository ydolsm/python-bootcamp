import tkinter

root = tkinter.Tk()

message = """
    Hello World
    In Multiple Lines
"""
#label = root refers to the window
label = tkinter.Label(root, text=message)
label.pack()

root.mainloop()