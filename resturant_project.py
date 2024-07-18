from tkinter import *
import random
import time
import datetime

app = Tk()
app.geometry("1600x8000")
app.title("Bistro Management System")

# Frame for the top section
top_frame = Frame(app, width=1600, relief=RAISED)
top_frame.pack(side=TOP)

# Frame for the left section
left_frame = Frame(app, width=800, height=700, relief=RAISED)
left_frame.pack(side=LEFT)

# Display current time
current_time = time.asctime(time.localtime(time.time()))

# Bistro name label
lblTitle = Label(top_frame, font=('times', 50, 'bold'), text="Bistro Haven", fg="DarkGreen", bd=10, anchor='w')
lblTitle.grid(row=0, column=0)

# Current time label
lblTime = Label(top_frame, font=('courier', 20, 'bold'), text=current_time, fg="Blue", bd=10, anchor='w')
lblTime.grid(row=1, column=0)

def calculate_bill():
    ref_number = random.randint(10000, 99999)
    ref.set(ref_number)

    fries_cost = float(fries_qty.get()) if fries_qty.get() else 0
    noodles_cost = float(noodles_qty.get()) if noodles_qty.get() else 0
    soup_cost = float(soup_qty.get()) if soup_qty.get() else 0
    burger_cost = float(burger_qty.get()) if burger_qty.get() else 0
    sandwich_cost = float(sandwich_qty.get()) if sandwich_qty.get() else 0
    drink_cost = float(drink_qty.get()) if drink_qty.get() else 0

    total_fries = fries_cost * 150
    total_drinks = drink_cost * 70
    total_noodles = noodles_cost * 95
    total_soup = soup_cost * 150
    total_burger = burger_cost * 270
    total_sandwich = sandwich_cost * 310

    subtotal = total_fries + total_drinks + total_noodles + total_soup + total_burger + total_sandwich
    service_charge = subtotal * 0.1
    tax = subtotal * 0.15
    total_cost = subtotal + service_charge + tax

    subtotal_var.set(f"₹ {subtotal:.2f}")
    service_var.set(f"₹ {service_charge:.2f}")
    tax_var.set(f"₹ {tax:.2f}")
    total_var.set(f"₹ {total_cost:.2f}")

def clear_fields():
    ref.set("")
    fries_qty.set("")
    noodles_qty.set("")
    soup_qty.set("")
    subtotal_var.set("")
    total_var.set("")
    service_var.set("")
    drink_qty.set("")
    tax_var.set("")
    cost_var.set("")
    burger_qty.set("")
    sandwich_qty.set("")

def exit_app():
    app.destroy()

# Variables to store inputs and calculated values
ref = StringVar()
fries_qty = StringVar()
noodles_qty = StringVar()
soup_qty = StringVar()
subtotal_var = StringVar()
total_var = StringVar()
service_var = StringVar()
drink_qty = StringVar()
tax_var = StringVar()
cost_var = StringVar()
burger_qty = StringVar()
sandwich_qty = StringVar()

# Labels and input fields
lblRef = Label(left_frame, font=('arial', 16, 'bold'), text="Order Ref", bd=16, anchor="w")
lblRef.grid(row=0, column=0)
txtRef = Entry(left_frame, font=('arial', 16, 'bold'), textvariable=ref, bd=10, insertwidth=4, bg="light yellow", justify='right')
txtRef.grid(row=0, column=1)

lblFries = Label(left_frame, font=('arial', 16, 'bold'), text="French Fries", bd=16, anchor="w")
lblFries.grid(row=1, column=0)
txtFries = Entry(left_frame, font=('arial', 16, 'bold'), textvariable=fries_qty, bd=10, insertwidth=4, bg="light yellow", justify='right')
txtFries.grid(row=1, column=1)

lblNoodles = Label(left_frame, font=('arial', 16, 'bold'), text="Chow Mein", bd=16, anchor="w")
lblNoodles.grid(row=2, column=0)
txtNoodles = Entry(left_frame, font=('arial', 16, 'bold'), textvariable=noodles_qty, bd=10, insertwidth=4, bg="light yellow", justify='right')
txtNoodles.grid(row=2, column=1)

lblSoup = Label(left_frame, font=('arial', 16, 'bold'), text="Hot Soup", bd=16, anchor="w")
lblSoup.grid(row=3, column=0)
txtSoup = Entry(left_frame, font=('arial', 16, 'bold'), textvariable=soup_qty, bd=10, insertwidth=4, bg="light yellow", justify='right')
txtSoup.grid(row=3, column=1)

lblBurger = Label(left_frame, font=('arial', 16, 'bold'), text="Cheese Burger", bd=16, anchor="w")
lblBurger.grid(row=4, column=0)
txtBurger = Entry(left_frame, font=('arial', 16, 'bold'), textvariable=burger_qty, bd=10, insertwidth=4, bg="light yellow", justify='right')
txtBurger.grid(row=4, column=1)

lblSandwich = Label(left_frame, font=('arial', 16, 'bold'), text="Grilled Sandwich", bd=16, anchor="w")
lblSandwich.grid(row=5, column=0)
txtSandwich = Entry(left_frame, font=('arial', 16, 'bold'), textvariable=sandwich_qty, bd=10, insertwidth=4, bg="light yellow", justify='right')
txtSandwich.grid(row=5, column=1)

lblDrinks = Label(left_frame, font=('arial', 16, 'bold'), text="Beverages", bd=16, anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks = Entry(left_frame, font=('arial', 16, 'bold'), textvariable=drink_qty, bd=10, insertwidth=4, bg="light yellow", justify='right')
txtDrinks.grid(row=0, column=3)

lblSubtotal = Label(left_frame, font=('arial', 16, 'bold'), text="Subtotal", bd=16, anchor="w")
lblSubtotal.grid(row=1, column=2)
txtSubtotal = Entry(left_frame, font=('arial', 16, 'bold'), textvariable=subtotal_var, bd=10, insertwidth=4, bg="light yellow", justify='right')
txtSubtotal.grid(row=1, column=3)

lblServiceCharge = Label(left_frame, font=('arial', 16, 'bold'), text="Service Charge", bd=16, anchor="w")
lblServiceCharge.grid(row=2, column=2)
txtServiceCharge = Entry(left_frame, font=('arial', 16, 'bold'), textvariable=service_var, bd=10, insertwidth=4, bg="light yellow", justify='right')
txtServiceCharge.grid(row=2, column=3)

lblTax = Label(left_frame, font=('arial', 16, 'bold'), text="Tax", bd=16, anchor="w")
lblTax.grid(row=3, column=2)
txtTax = Entry(left_frame, font=('arial', 16, 'bold'), textvariable=tax_var, bd=10, insertwidth=4, bg="light yellow", justify='right')
txtTax.grid(row=3, column=3)

lblTotal = Label(left_frame, font=('arial', 16, 'bold'), text="Total", bd=16, anchor="w")
lblTotal.grid(row=4, column=2)
txtTotal = Entry(left_frame, font=('arial', 16, 'bold'), textvariable=total_var, bd=10, insertwidth=4, bg="light yellow", justify='right')
txtTotal.grid(row=4, column=3)

# Buttons for Calculate, Reset, and Exit
btnCalculate = Button(left_frame, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Calculate", bg="light blue", command=calculate_bill)
btnCalculate.grid(row=7, column=1)

btnReset = Button(left_frame, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Reset", bg="light blue", command=clear_fields)
btnReset.grid(row=7, column=2)

btnExit = Button(left_frame, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Exit", bg="light blue", command=exit_app)
btnExit.grid(row=7, column=3)

app.mainloop()
