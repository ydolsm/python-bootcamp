import tkinter

# Create the main window
root = tkinter.Tk()

# Create an IntVar to hold the slider value
slider_value = tkinter.IntVar(root, 0)

# Create a label to display the slider value, linking it to the IntVar
value_label = tkinter.Label(root, textvariable=slider_value)
value_label.pack()

# Create a slider (Scale widget) and link it to the IntVar
slider = tkinter.Scale(root, from_=0, to=100, orient="horizontal", variable=slider_value)
slider.pack()

# Run the Tkinter event loop
root.mainloop()
