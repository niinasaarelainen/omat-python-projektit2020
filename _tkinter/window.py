from tkinter import *

window = Tk()

window.title("Welcome to LikeGeeks app")
window.geometry('350x200')

lbl = Label(window, text="Hello", font=("Arial Bold", 60))

lbl.grid(column=0, row=0)

window.mainloop()