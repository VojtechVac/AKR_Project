from tkinter import *

#pod toto pôjde kód

window = Tk()

window.title("Password Manager")

def loginScreen():
    window.geometry("640x360")
    okno = Label(window, text = "Vlož email")
    okno.config(anchor=CENTER)
    okno.pack()

    text = Entry(window, width = 20)
    text.pack()

    okno = Label(window, text = "Vlož heslo")
    okno.config(anchor=CENTER)
    okno.pack()

    text = Entry(window, width = 20)
    text.pack()

    def kontrolaHesla():
            print("test")

    tlacidlo = Button(window, text = "Potvrdiť", command = kontrolaHesla)
    tlacidlo.pack()
    
loginScreen()
window.mainloop()