import tkinter

root = tkinter.Tk()
#root.title("Password Checker")
root.geometry("400x300")

user_input = tkinter.StringVar(root, value="Enter any text")
label = tkinter.Label(root, textvariable=user_input)
label.pack()

entry = tkinter.Entry(root)
entry.pack()

def display(event):
    user_input.set(entry.get())

root.bind("<Return>", display)
root.mainloop()