import tkinter

root = tkinter.Tk()
#add window title
root.title("Haiku")
#define the window size
root.geometry("200x100")

message = """
    Loops within loops spin,
    A silent function returns,
    The logic is clear.
"""
#label = root refers to the window
label = tkinter.Label(root, text=message)
label.pack()

root.mainloop()