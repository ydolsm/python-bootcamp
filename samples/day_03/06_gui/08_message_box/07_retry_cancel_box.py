import tkinter
from tkinter import messagebox

# Set up the main window
root = tkinter.Tk()

# Trigger the messagebox directly
response = messagebox.askretrycancel("Ask Retry/Cancel", "Retry or Cancel?")
print("Response:", response)

root.mainloop()
