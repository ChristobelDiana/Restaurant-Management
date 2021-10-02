from tkinter import *
import random
from datetime import datetime
from PIL import Image, ImageTk

root = Tk()
root.geometry("1200x650+100+20")
root.title("Restaurant Management system")

f = Frame(root, bd=10, relief=GROOVE)
f.pack(side=TOP)

f1 = Frame(root, bd=5, height=400,width=300, relief=RAISED)
f1.pack(side=LEFT,fill="both", expand=1)

f2 = Frame(root, bd=5, height=400, width=300, relief=RAISED)

image = Image.open('dosa-idli.jpg')
tk_image = ImageTk.PhotoImage(image.resize((300,120)))

lbl_info = Label(f, font=('aria', 30, 'bold'), text="Restaurant Billing System",image=tk_image,fg="white",bg='brown',width=1150,compound='left')
lbl_info.grid(row=0, column=0)

now = datetime.now()
localtime = now.strftime("%d/%m/%Y %H:%M:%S")

rand = StringVar()
Dosa = StringVar()
Pongal = StringVar()
Vadai = StringVar()
Poori = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Idli = StringVar()
Tax = StringVar()
cost = StringVar()
date = StringVar()
Coffee = StringVar()
tea = StringVar()


lbl_Idli = Label(f1, font=('aria', 20, 'bold'), text="Idli Rs.30", width=12, fg="blue4", bd=10, anchor='w')
lbl_Idli.grid(row=1,column=0)
txt_Idli = Entry(f1,font=('ariel', 20,'bold'), textvariable=Idli, bd=6,width=8,bg="misty rose" ,justify='right')
txt_Idli.grid(row=1,column=1)

lbl_dosa = Label(f1, font=('aria', 20, 'bold'),text="Dosa Rs.45",width=12,fg="blue4",bd=10,anchor='w')
lbl_dosa.grid(row=2, column=0)
txt_dosa = Entry(f1,font=('ariel', 20, 'bold'), textvariable=Dosa , bd=6,width=8,bg="misty rose" ,justify='right')
txt_dosa.grid(row=2, column=1)

lbl_Pongal = Label(f1, font=('aria', 20,'bold'),text="Pongal Rs.55",width=12,fg="blue4",bd=10,anchor='w')
lbl_Pongal.grid(row=3, column=0)
txt_Pongal = Entry(f1, font=('ariel', 20, 'bold'), textvariable=Pongal , bd=6,width=8,bg="misty rose" ,justify='right')
txt_Pongal.grid(row=3, column=1)

lbl_vadai = Label(f1, font=('aria', 20,'bold'),text="Vadai Rs.20 ",width=12,fg="blue4",bd=10,anchor='w')
lbl_vadai.grid(row=4,column=0)
txt_vadai = Entry(f1,font=('ariel', 20,'bold'), textvariable=Vadai , bd=6,width=8,bg="misty rose" ,justify='right')
txt_vadai.grid(row=4,column=1)

lbl_Poori = Label(f1, font=('aria', 20,'bold'),text="Poori Rs.50",width=12,fg="blue4",bd=10,anchor='w')
lbl_Poori.grid(row=5,column=0)
txt_Poori = Entry(f1,font=('ariel', 20, 'bold'), textvariable=Poori, bd=6,width=8,bg="misty rose" ,justify='right')
txt_Poori.grid(row=5,column=1)

lbl_tea = Label(f1, font=('aria', 20, 'bold' ),text="Tea Rs.15",width=12,fg="blue4",bd=10,anchor='w')
lbl_tea.grid(row=6,column=0)
txt_tea = Entry(f1,font=('ariel', 20,'bold'), textvariable=tea, bd=6,width=8,bg="misty rose" ,justify='right')
txt_tea.grid(row=6,column=1)

lbl_coffee = Label(f1, font=('aria', 20, 'bold'), text="Coffee Rs.20", width=12,fg="blue4",bd=10,anchor='w')
lbl_coffee.grid(row=7,column=0)
txt_coffee = Entry(f1,font=('ariel', 20, 'bold'), textvariable=Coffee, bd=6,width=8,bg="misty rose" ,justify='right')
txt_coffee.grid(row=7,column=1)


def generate_bill():
    bill_no = str(random.randint(15000, 50000))
    rand.set(bill_no)
    date.set(localtime)
    try: qd = int(Dosa.get())
    except: qd = 0
    try: qp = int(Pongal.get())
    except:qp = 0
    try:qv = int(Vadai.get())
    except:qv = 0
    try: qpoori = int(Poori.get())
    except: qpoori = 0
    try: qcof = int(Coffee.get())
    except: qcof = 0
    try: qi = int(Idli.get())
    except:qi = 0
    try: qt = int(tea.get())
    except:qt = 0

    costofdosa = qd * 45
    costofPongal = qp * 55
    costofvadai = qv * 20
    costofPoori = qpoori * 50
    costofcoffee = qcof * 20
    costofidli = qi * 30
    costoftea = qt * 15

    f2.pack(side=RIGHT, fill="both", expand=1)
    f2.configure(background="light yellow")

    lbl_bill = Label(f2, font=('aria', 18, 'bold'), text="Bill No.", bg="light yellow", width=12, bd=20, anchor='w')
    lbl_bill.grid(row=1, column=0)
    txt_bill = Entry(f2, font=('ariel', 18, 'bold'), textvariable=rand, bd=6, width=17, bg="brown", fg='white',justify='right')
    txt_bill.grid(row=1, column=1)

    lbl_date = Label(f2, font=('aria', 18, 'bold'), text="Date", bg="light yellow", width=12, bd=10, anchor='w')
    lbl_date.grid(row=2, column=0)
    txt_date = Entry(f2, font=('ariel', 18, 'bold'), textvariable=date, bd=6, width=17, bg="Pale Green1", justify='right')
    txt_date.grid(row=2, column=1)

    lbl_cost = Label(f2, font=('aria', 18, 'bold'), text="Cost", bg="light yellow",width=12, bd=10, anchor='w')
    lbl_cost.grid(row=3, column=0)
    txt_cost = Entry(f2, font=('ariel', 18, 'bold'), textvariable=cost, bd=6, width=17, bg="Pale Green1", justify='right')
    txt_cost.grid(row=3, column=1)

    lbl_service = Label(f2, font=('aria', 18, 'bold'), text="Service Charge",bg="light yellow", width=12, bd=10, anchor='w')
    lbl_service.grid(row=4, column=0)
    txt_service = Entry(f2, font=('ariel', 18, 'bold'), textvariable=Service_Charge, bd=6, width=17, bg="Pale Green1", justify='right')
    txt_service.grid(row=4, column=1)

    lbl_tax = Label(f2, font=('aria', 18, 'bold'), text="Tax",bg="light yellow", width=12, bd=10, anchor='w')
    lbl_tax.grid(row=5, column=0)
    txt_tax = Entry(f2, font=('ariel', 18, 'bold'), textvariable=Tax, bd=6, width=17, bg="Pale Green1", justify='right')
    txt_tax.grid(row=5, column=1)

    lbl_total = Label(f2, font=('aria', 18, 'bold'), text="Total",bg="light yellow", width=12, bd=10, anchor='w')
    lbl_total.grid(row=6, column=0)
    txt_total = Entry(f2, font=('ariel', 18, 'bold'), textvariable=Total, bd=6, width=17, bg="brown", fg='white', justify='right')
    txt_total.grid(row=6, column=1)

    Totalcost= costofdosa + costoftea + costofPongal + costofvadai + costofPoori + costofcoffee + costofidli
    costofmeal = "Rs.", str('%.2f' % Totalcost)
    payTax = (Totalcost * 0.18)
    paidTax = "Rs.", str('%.2f' % payTax)
    ser_charge = (Totalcost * 0.01)
    service = "Rs.", str('%.2f' % ser_charge)
    overall = payTax + Totalcost + ser_charge
    total = "Rs.", str('%.2f' % overall)

    Service_Charge.set(service)
    cost.set(costofmeal)
    Tax.set(paidTax)
    Total.set(total)


def qexit():
    root.destroy()


def reset():
    Dosa.set('')
    Pongal.set('')
    Vadai.set('')
    Poori.set('')
    Idli.set('')
    date.set('')
    tea.set('')
    Coffee.set('')
    f2.pack_forget()


btn_Total = Button(f1, bd=5, fg="black",font=('ariel', 16, 'bold'), width=14, text="CALCULATE BILL", bg="SteelBlue1",command=generate_bill)
btn_Total.grid(row=9, column=0, padx=10, pady=10)

btn_reset = Button(f1, bd=5, fg="black", font=('ariel', 16, 'bold'), width=10, text="RESET", bg="SteelBlue1",command=reset)
btn_reset.grid(row=9, column=1, padx=10, pady=10)

btn_exit = Button(f1, bd=5, fg="black", font=('ariel', 16, 'bold'), width=10, text="EXIT", bg="SteelBlue1", command=qexit)
btn_exit.grid(row=9, column=2, padx=10, pady=10)

root.mainloop()