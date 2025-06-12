from tkinter import *

#setup vars
convert_list = {"len": 1.609344, "mass": 0.453592, "volume": 3.78541}
mode_text = {"len": "Length", "mass": "Mass", "temp": "Temperature", "volume": "Volume"}
mode_out_units = {"len": "km", "mass": "kg", "temp": "°C", "volume": "L"}
mode_in_units = {"len": "mi", "mass": "lb", "temp": "°F", "volume": "gal"}
mode="len"
modes_list = list(mode_text.keys())

#setup window
window = Tk()
window.title("Conversion Tool")
window.minsize(width=400, height=300)
label = Label(text=f"Mode: {mode}", font=("Arial", 24, "bold"))
label.grid(column=1, row=0)
converted_label = Label(text="")
converted_label.grid(column=2, row=3)
start_unit=Label(text=str(mode_in_units[mode]))
start_unit.grid(column=3, row=2)
end_unit=Label(text=str(mode_out_units[mode]))
end_unit.grid(column=3, row=3)
equals=Label(text="equals")
equals.grid(column=1,row=3)

#setup input
entry = Entry(width=10)
entry.grid(column=2, row=2)

def convert():
    if mode=="temp":
        converted = (int(entry.get()) - 32) * 5/9
    else:
        converted=round(convert_list[mode]*float(entry.get()),3)
    converted_label.config(text=str(converted))
def change_mode():
    global mode
    mode = modes_list[(modes_list.index(mode) + 1) % len(modes_list)]
    label.config(text=f"Mode: {mode}")
    start_unit.config(text=str(mode_in_units[mode]))
    end_unit.config(text=str(mode_out_units[mode]))

b1 = Button(text="Convert", width=10, command=convert)
b1.grid(column=0, row=1)
b2 = Button(text="Change Mode", width=10, command=change_mode)
b2.grid(column=1, row=1)
mode="len"
modes_list = list(mode_text.keys())
#end
window.mainloop()