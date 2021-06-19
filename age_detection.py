from tkinter import *
from datetime import date


gui= Tk()
gui.geometry("700x500")
gui.title("Age Calculator")

photo = PhotoImage(file="mac-os-logo(1).png")
myimage = Label(image = photo)
myimage.grid(row=0,column=1)
