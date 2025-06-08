import tkinter

root = tkinter.Tk()
root.geometry("400x300")

entry = tkinter.Entry(root)
entry.pack()

def mark_input(event):
    label = tkinter.Label(root, text=entry.get())
    label.pack()

root.bind("<Return>", mark_input)
root.mainloop()