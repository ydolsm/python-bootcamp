import tkinter

root = tkinter.Tk()
root.geometry("200x100")

count = tkinter.IntVar(root, value=0)
label = tkinter.Label(root, textvariable=count)
label.pack()

def increment():
    count.set(count.get() + 1)

button = tkinter.Button(root, text=" + ", command=increment)
button.pack(side="left")

def decrease():
    count.set(count.get() - 1)

button = tkinter.Button(root, text=" - ", command=decrease)
button.pack(side="right")

root.mainloop()