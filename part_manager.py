from tkinter import *


# Create window object
app = Tk()
app.title('Part Manager')
app.geometry('700x350')


# Part
part_text = StringVar()

part_label = Label(app, text='Part Name', font=("Courier", 12, 'bold'), pady=20)
part_label.grid(row=0, column=0, sticky=W)

part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)


# Customer
customer_text = StringVar()

customer_label = Label(app, text='Customer Name', font=("Courier", 12, 'bold'))
customer_label.grid(row=0, column=2, sticky=W)

customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0, column=3)


# Retailer
retailer_text = StringVar()

retailer_label = Label(app, text='Retailer Name', font=("Courier", 12, 'bold'))
retailer_label.grid(row=1, column=0, sticky=W)

retailer_entry = Entry(app, textvariable=retailer_text)
retailer_entry.grid(row=1, column=1)


# Price
price_text = StringVar()

price_label = Label(app, text='Price Name', font=("Courier", 12, 'bold'))
price_label.grid(row=1, column=2, sticky=W)

price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)


# Start program
app.mainloop()