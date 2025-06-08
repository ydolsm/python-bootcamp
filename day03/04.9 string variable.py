import tkinter

root = tkinter.Tk()
root.geometry("400x300")

text = tkinter.StringVar(root, value="Hello")
label = tkinter.Label(root, textvariable=text)
label.pack()

root.mainloop()