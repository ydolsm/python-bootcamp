import tkinter

root = tkinter.Tk()
root.title("Password Checker")
root.geometry("400x300")

label = tkinter.Label(root, text="Enter your password:")
label.pack()

entry = tkinter.Entry(root)
entry.pack()

pw_entry = tkinter.StringVar(root, value="Click Submit:")
label = tkinter.Label(root, textvariable=pw_entry)
label.pack()

#put 'event=None' to enable both bind and button
#event is for bind only
def display(event=None):
    if entry.get() == "universe":
        pw_entry.set("Access granted!")
    else:
        pw_entry.set("Access denied!")

root.bind("<Return>", display)
button = tkinter.Button(root, text="Submit", command=display)
button.pack()
root.mainloop()