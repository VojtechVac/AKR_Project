from email_pokus import sendEmail
import os
from sys import platform

def clearscreen():
    if platform == 'win32':
        os.system('cls') 
    elif platform == 'darwin':
        os.system('clear') 
    elif platform == 'linux':
        os.system('clear') 
    
def menu():
      print("1. Zobrazit hesla")
      print("2. Pridat heslo")
      print("3. Zmazat heslo")
      print("0. Exit")


print("vlož email: ")
se = sendEmail()
se.send_email(input()) 
print("Zadaj kód:")
x = input()

if x == str(se.getMessage()):
    print("Správny kód")
    input("====Stlač enter====")
    # MENU
    clearscreen()
    menu()
    volba = int(input("Zvol moznost:"))

    while volba != 0:
        if volba == 1:
            print("Zvolil si zobrazenie hesiel")
            input("====Stlač enter====")
        elif volba == 2:
            print("Zvolil si pridanie hesla.")
            input("====Stlač enter====")
        elif volba == 3:
            print("Zvolil si zmazanie hesla")
            input("====Stlač enter====")
        else:
            print("Nespravna volba.")
            input("====Stlač enter====")

        clearscreen()
        menu()
        try:
            volba = int(input("Zvol moznost:"))
        except:
            print("Nespravny input.")
            break
    print("Exit.")


elif x != str(se.getMessage()):
    print("Nesprávny kód")
