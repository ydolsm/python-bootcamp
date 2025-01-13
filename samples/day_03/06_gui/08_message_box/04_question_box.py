import tkinter
from tkinter import messagebox

# Set up the main window
root = tkinter.Tk()

# Trigger the messagebox directly
response = messagebox.askquestion("Question", "Do you want to continue?", a=1, b=2)
print("Response:", response)

root.mainloop()
