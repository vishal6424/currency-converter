# from exchange_rates_data import data
#
# print(data)
import pandas as pd
from tkinter import *
from csv_modification import country_name
rate = pd.read_csv("country_name.csv")

window = Tk()
window.title("Currency Converter")
window.minsize(width=900, height=600)
window.config(padx=50, pady=10)


label1 = Label(text="COUNTRIES", font=("Arial", 10, "bold"))
label1.grid(row=0, column=0)
country = Label(text=country_name, font=("Arial", 7, "bold"))
country.grid(row=1, column=0)


label2 = Label(text="FROM\n(serial number)", font=("Arial", 20, "bold"))
label2.place(x=200, y=250)
#
label3 = Label(text="TO\n(serial number)", font=("Arial", 20, "bold"))
label3.place(x=500, y=250)


def spinbox_used_form():
    # gets the current value in spinbox.
    global rate
    index = int(spinbox_from.get())
    print(rate['1.00 USD'][index])
    label4.config(text=f"{rate['US Dollar'][index]}", font=("Arial", 20, "bold"))


spinbox_from = Spinbox(from_=0, to=52, width=15, command=spinbox_used_form)
spinbox_from.place(x=350, y=257)


def convert():
    global rate
    amount = float(amount_from.get())
    from_rate = float(rate['inv. 1.00 USD'][int(spinbox_from.get())])
    to_rate = float(rate['inv. 1.00 USD'][int(spinbox_to.get())])

    final = (amount * from_rate)/to_rate
    converted.config(text=f"{round(final, 2)}", font=("Arial", 20, "bold"))



def spinbox_used_to():
    # gets the current value in spinbox.
    global rate
    index = int(spinbox_to.get())
    print(rate['US Dollar'][index])
    label5.config(text=f"{rate['US Dollar'][index]}", font=("Arial", 20, "bold"))


spinbox_to = Spinbox(from_=0, to=52, width=15, command=spinbox_used_to)
spinbox_to.place(x=630, y=257)

label4 = Label(text=f"{rate['US Dollar'][0]}", font=("Arial", 20, "bold"))
label4.place(x=250, y=350)
#
label5 = Label(text=f"{rate['US Dollar'][0]}", font=("Arial", 20, "bold"))
label5.place(x=580, y=350)

amount_from = Entry()
# Puts cursor in textbox.
# amount_from.focus()
# Adds some text to begin with.
# amount_from.insert(END, "Enter the Amount ")
amount_from.place(x=255, y=410)

converted = Label(text="0", font=("Arial", 20, "bold"))
converted.place(x=580, y=400)


calculate = Button(text="CONVERT", command=convert, bg="red", font=("Arial", 10, "bold"))
calculate.place(x=460, y=410)



window.mainloop()
