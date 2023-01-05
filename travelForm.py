from tkinter import *

root = Tk()

def getVals():
    print(nameValue.get())
    print(phoneValue.get())
    print(genderValue.get())
    print(emergancyContactValue.get())
    print(paymentModeValue.get())
    print(foodServiceValue.get())

root.geometry("644x344")
Label(root,text="Our Travel Agency", font="comicsansms 13 bold").grid(row=0, column=3)
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergancyContact = Label(root, text="Emergncy contact")
paymentMode = Label(root, text="Payment mode")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergancyContact.grid(row=4, column=2)
paymentMode.grid(row=5, column=2)

nameValue = StringVar()
phoneValue = StringVar()
genderValue = StringVar()
emergancyContactValue = StringVar()
paymentModeValue = StringVar()
foodServiceValue = IntVar()

nameEntry = Entry(root, textvariable=nameValue)
phoneEntry = Entry(root, textvariable=phoneValue)
genderEntry = Entry(root, textvariable=genderValue)
emergancyContactEntry = Entry(root, textvariable=emergancyContactValue)
paymentModeEntry = Entry(root, textvariable=paymentModeValue)

nameEntry.grid(row=1, column=3)
phoneEntry.grid(row=2, column=3)
genderEntry.grid(row=3, column=3)
emergancyContactEntry.grid(row=4, column=3)
paymentModeEntry.grid(row=5, column=3)

# check box
foodService = Checkbutton(text="want to prebook your meals?", variable=foodServiceValue)
foodService.grid(row=6,column=3)


Button(text="Submit", command=getVals).grid(row=7, column=3)

root.mainloop()