import tkinter

def on_keypress(event):
    print(f"Key pressed: {event.keysym}")

root = tkinter.Tk()

# Bind alphanumeric keys
root.bind("<a>", on_keypress)
root.bind("<b>", on_keypress)
root.bind("<c>", on_keypress)

# Add more for the rest of the alphabet and numbers as needed
root.bind("<0>", on_keypress)
root.bind("<1>", on_keypress)

# Bind special keys
root.bind("<BackSpace>", on_keypress)
root.bind("<Tab>", on_keypress)
root.bind("<Return>", on_keypress)
root.bind("<Shift_L>", on_keypress)
root.bind("<Control_L>", on_keypress)
root.bind("<Alt_L>", on_keypress)
root.bind("<Caps_Lock>", on_keypress)
root.bind("<Escape>", on_keypress)
root.bind("<Delete>", on_keypress)
root.bind("<Insert>", on_keypress)
root.bind("<Home>", on_keypress)
root.bind("<End>", on_keypress)
root.bind("<Page_Up>", on_keypress)
root.bind("<Page_Down>", on_keypress)

# Note: Space is oddly lowercase
root.bind("<space>", on_keypress)

# Bind function keys
root.bind("<F1>", on_keypress)
root.bind("<F2>", on_keypress)
root.bind("<F3>", on_keypress)
root.bind("<F4>", on_keypress)
root.bind("<F5>", on_keypress)
root.bind("<F6>", on_keypress)
root.bind("<F7>", on_keypress)
root.bind("<F8>", on_keypress)
root.bind("<F9>", on_keypress)
root.bind("<F10>", on_keypress)
root.bind("<F11>", on_keypress)
root.bind("<F12>", on_keypress)

# Bind navigation keys
root.bind("<Left>", on_keypress)
root.bind("<Right>", on_keypress)
root.bind("<Up>", on_keypress)
root.bind("<Down>", on_keypress)

# Bind modifier keys
root.bind("<Shift_R>", on_keypress)
root.bind("<Control_R>", on_keypress)
root.bind("<Alt_R>", on_keypress)

# Bind other keys
root.bind("<Pause>", on_keypress)
root.bind("<Print>", on_keypress)
root.bind("<Num_Lock>", on_keypress)
root.bind("<Scroll_Lock>", on_keypress)

root.mainloop()
