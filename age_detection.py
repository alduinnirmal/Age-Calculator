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

