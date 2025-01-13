import tkinter as tk


reliefs = ["flat", "raised", "sunken", "groove", "ridge", "solid"]
root = tk.Tk()

for relief in reliefs:
    label = tk.Label(root, text=relief.capitalize(), borderwidth=5, relief=relief, bg='lightblue')
    label.pack(pady=5)

root.mainloop()