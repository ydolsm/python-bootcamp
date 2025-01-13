import tkinter
root = tkinter.Tk()

label1 = tkinter.Label(root, text="Label 1")
label1.grid(row=0, column=0, padx=10, pady=10)

label2 = tkinter.Label(root, text="Label 2")
label2.grid(row=0, column=1, padx=10, pady=10)

label3 = tkinter.Label(root, text="Label 3")
label3.grid(row=1, column=0, padx=10, pady=10)

label4= tkinter.Label(root, text="Label 4")
label4.grid(row=1, column=1, padx=10, pady=10)

button = tkinter.Button(root, text="Click Me")
button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()


