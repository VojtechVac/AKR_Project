from PIL import Image
import pyotp
import qrcode
from IPython.display import display
from tkinter import *  

#generuje nahodný 16bit kľuč (asi)
secrete_key = pyotp.TOTP("3232323232323232")
print(secrete_key.now())

#nie som si isty čo tato kravina robí ale niečo to robí z čoho sa vytvorí nižšie QR code
auth_info = secrete_key.provisioning_uri(name = "som chuj", issuer_name = "PasswordManager")
#print(auth_info)

"""vytvorenie QR kodu, nasledne ho to uloží do FILU (aby vam to šlo musite si tam zmeniť cestu k suboru)
to chcem ešte doriešiť aby sa to neukladalo ale hned len zobrazilo"""
qr_code = qrcode.make(auth_info)
print(type(qr_code))
qr_code.save("/Users/oliverbielik/Documents/akrprojekt/AKR_Project/QR_CODES/qr_code_obrazok.png")


"""toto otvorí okno v ktorom zobrazí QR kód ktorý sa dá nasnímať cez tu google apku -
Google Authenticator, zatial otvára obrázok zo suboru to chcem ešte doriešiť aby otvaral
priamo a neukladal to do súboru"""
root = Tk()      
canvas = Canvas(root, width = 500, height = 500)      
canvas.pack()      
img = PhotoImage(file="/Users/oliverbielik/Documents/akrprojekt/AKR_Project/QR_CODES/qr_code_obrazok.png")      
canvas.create_image(20,20, anchor=NW, image=img)      
mainloop()   