from email_pokus import sendEmail
from login import Login
import os
from sys import platform
import sqlite3
import hashlib

from login import Login

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

def pwVerify(password):
    pw = password.encode('utf-8')
    hashed = hashlib.sha256(pw).hexdigest()
    if login.getHash() == hashed:
        return True
    else:
        return False

#PREMENNE
mail = ""
password = ""

conn = sqlite3.connect('users.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS users (
            mail text,
            password text
            )""")

#Tuto sa user prihlasuje, ma 5 pokusov zadat spravne heslo
"""for i in range(5):
    print("Zadaj heslo:")
    password = input()
    if pwVerify(password) == True:
        clearscreen()
        print("Vitajte.")
        break
    elif pwVerify(password) != True:
        clearscreen()
        print("Skus znova.")
    elif i == 4:
        print("Prilis vela pokusov")
"""

print("vlož email: ")
mail = input()
password = input()
#Hash hesla
login = Login(mail, password)
login.hashPassword()

#Vlozenie mailu a hashu hesla do databazy cez preparedstatement
c.execute("""INSERT INTO users ('mail', 'password') VALUES (?, ?);""", (mail, login.getHash()))
conn.commit()

#Print databazy
for row in c.execute('SELECT * FROM users;'):
    print(row)

#Posielanie mailu, DOCASNE VYPNUTE
#se = sendEmail()
#se.send_email(mail) 
print("Zadaj kod:")
x = input()

if x == str(se.getMessage()):
    print("Spravny kod")
    input("====Stlač enter====")
    # MENU
    clearscreen()
    menu()
    volba = int(input("Zvol moznost:"))

    while volba != 0:
        if volba == 1:
            print("Zvolil si zobrazenie hesiel")
            input("====Stlac enter====")
        elif volba == 2:
            print("Zvolil si pridanie hesla.")
            input("====Stlac enter====")
        elif volba == 3:
            print("Zvolil si zmazanie hesla")
            input("====Stlac enter====")
        else:
            print("Nespravna volba.")
            input("====Stlac enter====")

        clearscreen()
        menu()
        try:
            volba = int(input("Zvol moznost:"))
        except:
            print("Nespravny input.")
            break
    print("Exit.")
    
    conn.close()

elif x != str(se.getMessage()):
    print("Nespravny kod")
