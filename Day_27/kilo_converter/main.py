from tkinter import *


def button_clicked():
    # get mile
    input_mile = float(input.get())
    # calculate
    output_km = calculate(input_mile)
    # show result
    km_value.config(text=output_km)


def calculate(mile):
    kilo = round(mile * 1.6)
    return kilo


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
# miles
miles = Label(text="Miles")
miles.grid(column=2, row=0)

# km
km = Label(text="Km")
km.grid(column=2, row=1)

# is_equal_to
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

# km_value
km_value = Label()
km_value.grid(column=1, row=1)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

# Entry
input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()
