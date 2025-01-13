import tkinter
from tkinter import messagebox

# Set up the main window
root = tkinter.Tk()

# Trigger the messagebox directly
response = messagebox.askyesno("Ask Yes/No", "Do you agree?")
print("Response:", response)

root.mainloop()
