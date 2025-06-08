import tkinter
import json

root = tkinter.Tk()
root.title("User Form")
root.geometry("400x300")

#name entry
label_name = tkinter.Label(root, text="Name")
label_name.pack()

input_name = tkinter.Entry(root)
input_name.pack()

#age entry
label_age = tkinter.Label(root, text="Age")
label_age.pack()

input_age = tkinter.Entry(root)
input_age.pack()

#preferred theme selection - radio button
label_theme = tkinter.Label(root, text="Preferred Theme")
label_theme.pack()

select_theme = tkinter.StringVar(value="Light")
radio1 = tkinter.Radiobutton(
root, text="Light", variable=select_theme, value="Light")
radio2 = tkinter.Radiobutton(
root, text="Dark", variable=select_theme, value="Dark")
radio1.pack()
radio2.pack()

#subscription option - checkbox
subscribe_value = tkinter.BooleanVar()
checkbox = tkinter.Checkbutton(
    root,
    text="Subscribe to newsletter",
variable=subscribe_value
)
checkbox.pack()

#rating selection - slider
label_theme = tkinter.Label(root, text="Rate us")
label_theme.pack()

rating = tkinter.IntVar(value=0)
slider = tkinter.Scale(
    root,
    from_=1,
    to=3,
    orient="horizontal",
    variable=rating
)
slider.pack()

#create json file
def get_userinfo():
    user_info = {
        "Name": input_name.get(),
        "Age": input_age.get(),
        "Theme": select_theme.get(),
        "Subscribe": subscribe_value.get(),
        "Rating": rating.get()
    }

    with open('user.json', 'w') as file:
        json.dump(user_info, file, indent=4)

button = tkinter.Button(root, text="Submit", command=get_userinfo)
button.pack()

root.mainloop()
