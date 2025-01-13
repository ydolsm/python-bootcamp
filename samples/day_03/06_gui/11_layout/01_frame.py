import tkinter as tk

root = tk.Tk()

top_frame = tk.Frame(root, bg="lightblue", height=100)
top_frame.pack(fill="x")

bottom_frame = tk.Frame(root, bg="lightgreen", height=200)
bottom_frame.pack(fill="both", expand=True)

label1 = tk.Label(top_frame, text="Top Frame", bg="blue")
label1.pack(pady=10)

label2 = tk.Label(bottom_frame, text="Bot Frame", bg="green")
label2.pack(pady=20)

button = tk.Button(bottom_frame, text="Click Me")
button.pack(pady=10)

root.mainloop()
