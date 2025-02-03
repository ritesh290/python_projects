from tkinter import *

window=Tk()

window.geometry("400x400")

window.title("MyApplication")

photo=PhotoImage(file=r"c:\Users\AI\Pictures\flower.png")

window.iconphoto(False,photo)

window.config(background="#9FE2BF")



window.mainloop()