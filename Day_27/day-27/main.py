from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label

my_label = Label(text="I am a label", font=("Arial", 24, "italic"))
my_label.pack(side="bottom", expand=True)

my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button


def button_clicked():
    print("I got clicked.")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry

input = Entry(width=10)
input.pack()
print(input.get())


window.mainloop()
