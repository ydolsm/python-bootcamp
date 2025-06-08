import tkinter

root = tkinter.Tk()
#add window title
root.title("Sample GUI Application")
#define the window size
root.geometry("1200x400")

message = """
    Hello World
    In Multiple Lines
"""
#label - root refers to the window
#properties - font, background color, etc
label = tkinter.Label(
    root,
    text=message,
    font=("Caviar Dreams", "14", "bold italic"),
    width=100,
    height=20,
    padx=10,
    pady=200,
    fg="white",
    bg="black",
    )
label.pack()

root.mainloop()