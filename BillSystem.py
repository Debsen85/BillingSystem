# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
import random 
import time
import datetime

root = Tk()
root.geometry("1366x768")
root.title("Billing Machine")

Tops = Frame(root, width=1350, height=750, bd=0, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width=900, height=525, bd=0, relief="raise")
f1.pack(side=LEFT)
f2 = Frame(root, width=440, height=525, bd=1, relief="raise")
f2.pack(side=TOP)

f1a = Frame(f1, width=900, height=330, bd=0, relief="raise")
f1a.pack(side=TOP)
f2a = Frame(f1, width=900, height=320, bd=0, relief="raise")
f2a.pack(side=BOTTOM)

f1aa = Frame(f1a, width=400, height=430, bd=0, relief="raise")
f1aa.pack(side=LEFT)
f1ab = Frame(f1a, width=400, height=430, bd=0, relief="raise")
f1ab.pack(side=RIGHT)

f2aa = Frame(f2a, width=450, height=330, bd=0, relief="raise")
f2aa.pack(side=LEFT)
f2ab = Frame(f2a, width=450, height=330, bd=1, relief="raise")
f2ab.pack(side=RIGHT)

lblInfo=Label(Tops, font=('arial',60,'bold'), text="          Online Billing System          ", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)	

#====Calculator=====

text_Input = StringVar()
operator=""
PaymentRef = StringVar()
pizza = StringVar()
burger = StringVar()
drink = StringVar()
HomeDelivery = StringVar()
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
Costofpizza = StringVar()
Costofburger = StringVar()
Costofdrink = StringVar()
CostofDelivery = StringVar()
DateofOrder = StringVar()

pizza.set(0)
burger.set(0)
drink.set(0)
HomeDelivery.set(0)
DateofOrder.set(time.strftime("%d/%m/%Y"))

def CostOfOrder():
	pizzaPrice = float(pizza.get())
	drinkPrice = float(drink.get())
	burgerPrice = float(burger.get())
	DeliveryCost = float(HomeDelivery.get())

	pizzaCost = "₹", str('%.2f'%((pizzaPrice * 15.50)))
	Costofpizza.set(pizzaCost)

	drinkCost = "₹", str('%.2f'%((drinkPrice * 7.49)))
	Costofdrink.set(drinkCost)

	burgerCost = "₹", str('%.2f'%((burgerPrice * 5.50)))
	Costofburger.set(burgerCost)

	Delivery = "₹", str('%.2f'%((DeliveryCost * 4.50)))
	CostofDelivery.set(Delivery)

	ToC = "₹", str('%.2f'%((pizzaPrice * 15.50) + (drinkPrice * 7.49) + (burgerPrice * 5.50) + (DeliveryCost * 4.50)))
	SubTotal.set(ToC)
	Tax = "₹", str('%.2f'%(((pizzaPrice * 15.50) + (drinkPrice * 7.49) + (burgerPrice * 5.50) + (DeliveryCost * 4.50)) * 0.2))
	PaidTax.set(Tax)
	TaxPay = (((pizzaPrice * 15.50)+(drinkPrice * 7.49) + (burgerPrice * 5.50) + (DeliveryCost * 4.50)) * 0.2)
	Cost = ((pizzaPrice * 15.50) + (drinkPrice * 7.49) + (burgerPrice * 5.50) + (DeliveryCost * 4.50))
	CostofItems = "₹", str('%.2f'%(TaxPay + Cost))
	TotalCost.set(CostofItems)

	x = random.randint(10034, 699812)
	randomRef = str(x)
	PaymentRef.set("BILL" + randomRef)

def PayReference():
	x = random.randint(10034, 699812)
	randomRef = str(x)
	PaymentRef.set("BILL" + randomRef)


def iExit():
	qExit = messagebox.askyesno("Billing System", "Do you want to exit the system")
	if qExit > 0:
		root.destroy()
		return

def Reset():
	PaymentRef.set("")
	pizza.set(0)
	burger.set(0)
	drink.set(0)
	HomeDelivery.set(0)
	PaidTax.set("")
	SubTotal.set("")
	TotalCost.set("")
	Costofpizza.set("")
	Costofdrink.set("")
	Costofburger.set("")
	CostofDelivery.set("")

def btnClick(numbers):
	global operator
	operator = operator + str(numbers)
	text_Input.set(operator)

def btnClearDisplay():
	global operator
	operator=""
	text_Input.set("")

def btnEqualsInput():
	global operator
	sumup = str(eval(operator))
	text_Input.set(sumup)
	operator=""

txtDisplay = Entry(f2, font=('arial',20, 'bold'), textvariable=text_Input, bd=5, insertwidth=9, justify='right')
txtDisplay.grid(columnspan=4)
btn7=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),text="7",command=lambda:btnClick(7)).grid(row=1, column=0)
btn8=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),text="8",command=lambda:btnClick(8)).grid(row=1, column=1)
btn9=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),text="9",command=lambda:btnClick(9)).grid(row=1, column=2)
btnplus=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),text="+",command=lambda:btnClick("+")).grid(row=1, column=3)

btn4=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),text="4",command=lambda:btnClick(4)).grid(row=3, column=0)
btn5=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),text="5",command=lambda:btnClick(5)).grid(row=3, column=1)
btn6=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),text="6",command=lambda:btnClick(6)).grid(row=3, column=2)
btnSub=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),text="-",command=lambda:btnClick("-")).grid(row=3, column=3)

btn1=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),text="1",command=lambda:btnClick(1)).grid(row=4, column=0)
btn2=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),text="2",command=lambda:btnClick(2)).grid(row=4, column=1)
btn3=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),text="3",command=lambda:btnClick(3)).grid(row=4, column=2)
btnMult=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),text="*",command=lambda:btnClick("*")).grid(row=4, column=3)

btn0=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),text="0",command=lambda:btnClick(0)).grid(row=5, column=0)
btnClear=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),text="C",command=btnClearDisplay).grid(row=5, column=1)
btnEquals=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),text="=",command=btnEqualsInput).grid(row=5, column=2)
btnDiv=Button(f2, padx=16, pady=16, bd=8, fg="black", font=('arial',20,'bold'),text="/",command=lambda:btnClick("/")).grid(row=5, column=3)

lblRef=Label(f1aa, font=('arial',16,'bold'), text="Sales Reference", bd=16, justify='left')
lblRef.grid(row=0,column=0)
txtRef=Entry(f1aa, font=('arial',16,'bold'), textvariable=PaymentRef, bd=5, insertwidth=2, justify='left')
txtRef.grid(row=0, column=1)

lblpizza=Label(f1aa, font=('arial',16,'bold'), text="Pizza", bd=16, anchor='w')
lblpizza.grid(row=1,column=0)
txtpizza=Entry(f1aa, font=('arial',16,'bold'), textvariable=pizza, bd=5, insertwidth=2, justify='left')
txtpizza.grid(row=1, column=1)

lblburger=Label(f1aa, font=('arial',16,'bold'), text="Burger", bd=16, anchor='w')
lblburger.grid(row=2,column=0)
txtburger=Entry(f1aa, font=('arial',16,'bold'), textvariable=burger, bd=5, insertwidth=2, justify='left')
txtburger.grid(row=2, column=1)

lbldrink=Label(f1aa, font=('arial',16,'bold'), text="Cold Drinks", bd=16, anchor='w')
lbldrink.grid(row=3,column=0)
txtdrink=Entry(f1aa, font=('arial',16,'bold'), textvariable=drink, bd=5, insertwidth=2, justify='left')
txtdrink.grid(row=3, column=1)

lblHomeDelivery=Label(f1aa, font=('arial',16,'bold'), text="Home Delivery", bd=16, anchor='w')
lblHomeDelivery.grid(row=4,column=0)
txtHomeDelivery=Entry(f1aa, font=('arial',16,'bold'), textvariable=HomeDelivery, bd=5, insertwidth=2, justify='left')
txtHomeDelivery.grid(row=4, column=1)

lblDateofOrder=Label(f1ab, font=('arial',16,'bold'), text="Date of Order", bd=16, anchor='w')
lblDateofOrder.grid(row=0,column=0)
txtDateofOrder=Entry(f1ab, font=('arial',16,'bold'), textvariable=DateofOrder, bd=5, insertwidth=2, justify='left')
txtDateofOrder.grid(row=0, column=1)

lblCostofpizza=Label(f1ab, font=('arial',16,'bold'), text="Cost of Pizza", bd=16, anchor='w')
lblCostofpizza.grid(row=1,column=0)
txtCostofpizza=Entry(f1ab, font=('arial',16,'bold'), textvariable=Costofpizza, bd=5, insertwidth=2, justify='left')
txtCostofpizza.grid(row=1, column=1)

lblCostofburger=Label(f1ab, font=('arial',16,'bold'), text="Cost of Burger", bd=16, anchor='w')
lblCostofburger.grid(row=2,column=0)
txtCostofburger=Entry(f1ab, font=('arial',16,'bold'), textvariable=Costofburger, bd=5, insertwidth=2, justify='left')
txtCostofburger.grid(row=2, column=1)

lblCostofdrink=Label(f1ab, font=('arial',16,'bold'), text="Cost of Cold Drinks", bd=16, anchor='w')
lblCostofdrink.grid(row=3,column=0)
txtCostofdrink=Entry(f1ab, font=('arial',16,'bold'), textvariable=Costofdrink, bd=5, insertwidth=2, justify='left')
txtCostofdrink.grid(row=3, column=1)

lblCostofDelivery=Label(f1ab, font=('arial',16,'bold'), text="Cost of Delivery", bd=16, anchor='w')
lblCostofDelivery.grid(row=4,column=0)
txtCostofDelivery=Entry(f1ab, font=('arial',16,'bold'), textvariable=CostofDelivery, bd=5, insertwidth=2, justify='left')
txtCostofDelivery.grid(row=4, column=1)

lblPaidTax=Label(f2aa, font=('arial',16,'bold'), text="Paid Tax", bd=16, anchor='w')
lblPaidTax.grid(row=2,column=0)
txtPaidTax=Entry(f2aa, font=('arial',16,'bold'), textvariable=PaidTax, bd=5, insertwidth=2, justify='left')
txtPaidTax.grid(row=2, column=1)

lblSubTotal=Label(f2aa, font=('arial',16,'bold'), text="Sub Total", bd=16, anchor='w')
lblSubTotal.grid(row=3,column=0)
txtSubTotal=Entry(f2aa, font=('arial',16,'bold'), textvariable=SubTotal, bd=5, insertwidth=2, justify='left')
txtSubTotal.grid(row=3, column=1)

lblTotalCost=Label(f2aa, font=('arial',16,'bold'), text="Total Cost", bd=16, anchor='w')
lblTotalCost.grid(row=4,column=0)
txtTotalCost=Entry(f2aa, font=('arial',16,'bold'), textvariable=TotalCost, bd=5, insertwidth=2, justify='left')
txtTotalCost.grid(row=4, column=1)

btnTotal=Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('arial',16,'bold'), width=20, text="Total Cost", command=CostOfOrder).grid(row=0, column=0)
btnRefer=Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('arial',16,'bold'), width=20, text="Sales Reference", command=PayReference).grid(row=0, column=1)
btnReset=Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('arial',16,'bold'), width=20, text="Reset", command=Reset).grid(row=1, column=0)
btnExit=Button(f2ab, padx=16, pady=16, bd=8, fg="black", font=('arial',16,'bold'), width=20, text="Exit", command=iExit).grid(row=1, column=1)

root.mainloop()
