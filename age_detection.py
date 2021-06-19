from tkinter import *
from datetime import date


gui= Tk()
gui.geometry("700x500")
gui.title("Age Calculator")


photo = PhotoImage(file="mac-os.png")
myimage = Label(image = photo)
myimage.grid(row=0,column=1)


def calculateAge():
    today = date.today()
    birthDate = date(int(yearEntry.get())),
    int(monthEntry.get()), int(dayEntry.get())
    age = today.year - birthDate.year - ((today.month,today.day) < (birthDate.month, birthDate.day))

    Label(text=f"{nameValue.get()} your age is {age}").grid(row = 6, column = 1)
    Label(text="Name").grid(row=1, column=0, padx=90)
    Label(text="Year").grid(row=2, column=0)
    Label(text="Month").grid(row=3, column=0)
    Label(text="Date").grid(row=4, column=0)


    nameValue = StringVar()
    yearValue = StringVar()
    monthValue = StringVar()
    dayValue = StringVar()


    nameEntry = Entry(gui, textvariable = nameValue)
    yearEntry = Entry(gui, textvariable= yearValue)
    monthEntry = Entry(gui, textvariable= monthValue)
    dayEntry = Entry(gui, textvariable= dayValue)


    nameEntry.grid(row=1, coloumn=1, pady=10)
    yearEntry.grid(row=1, coloumn=1, pady=10)
    monthEntry.grid(row=1, coloumn=1, pady=10)
    dayEntry.grid(row=1, coloumn=1, pady=10)


    Button(text="Calculate age", command=calculateAge).grid(row=5, coloumn=1, pady=10)


    gui.mainloop()







