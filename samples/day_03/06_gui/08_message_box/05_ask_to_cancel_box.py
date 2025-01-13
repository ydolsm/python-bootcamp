import tkinter as tk
from tkinter import messagebox

# Set up the main window
root = tk.Tk()

# Trigger the messagebox directly
response = messagebox.askokcancel("Ask OK/Cancel", "Do you want to proceed?")
print("Response:", response)

root.mainloop()