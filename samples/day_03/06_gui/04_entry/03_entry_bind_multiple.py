import tkinter

# Create the main window
root = tkinter.Tk()
root.title("Sample GUI Application")
root.geometry("400x400")

# Create an entry field
entry = tkinter.Entry(root)
entry.pack()

label = tkinter.Label(text="")
label.pack()

def show_input(event):
    user_input = entry.get()
    label.config(text=user_input)

entry.bind("<Return>", show_input)
entry.bind("<space>", show_input)

# Run the application
root.mainloop()