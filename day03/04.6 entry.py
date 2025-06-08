import tkinter

root = tkinter.Tk()

def print_left(event):
    print("Left pressed")

entry = tkinter.Entry(root)
entry.pack()

root.bind("<Left>", print_left)
root.mainloop()

