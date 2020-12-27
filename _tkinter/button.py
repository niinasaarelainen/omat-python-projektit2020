from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")

window.geometry('450x200')

lbl = Label(window, text="Hello", font=("Arial Bold", 17))

lbl.grid(column=0, row=0)

def clicked():

    lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Click Me", font=("Arial Bold", 20), command=clicked,  bg="black", fg="yellow")

btn.grid(column=1, row=0)

window.mainloop()