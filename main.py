from email_pokus import sendEmail
from login import Login
import os
from sys import platform
import sqlite3
import hashlib
import getpass
from login import Login
import logging

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
      print("0. Odhlasit")

def pwVerify(password):
    pw = password.encode('utf-8')
    hashed = hashlib.sha256(pw).hexdigest()
    if login.getHash() == hashed:
        return True
    else:
        return False

def firstScreen():
    print("1. Prihlasit sa")
    print("2. Registrovat sa")
    print("0. Exit")

#PREMENNE
mail = ""
password = ""
logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

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
        logger.info("Wrong password")
"""

firstScreen()
choice = int(input("Zvol moznost:"))
while choice != 0:
    if choice == 1:
        clearscreen()
        logger.info("Log in chosen")
        print("Zadaj email: ")
        mail = input()
        password = getpass.getpass(prompt='Zadaj heslo:')
        #Hash hesla
        login = Login(mail, password)
        login.hashPassword()

        #Vlozenie mailu a hashu hesla do databazy cez preparedstatement, DOCASNE VYPNUTE
        #c.execute("""INSERT INTO users ('mail', 'password') VALUES (?, ?);""", (mail, login.getHash()))
        #conn.commit()
        
        clearscreen()

        #Posielanie mailu, DOCASNE VYPNUTE
        se = sendEmail()
        se.send_email(mail) 
        print("Zadaj kod:")
        x = input()

        if x == str(se.getMessage()):
            print("Spravny kod")
            logger.info("Successful login")
            input("====Stlač enter====")
            clearscreen()
            menu()
            volba = int(input("Zvol moznost:"))

            while volba != 0:
                if volba == 1:
                    print("Zvolil si zobrazenie hesiel")
                    logger.info("Passwords viewed")
                    input("====Stlac enter====")
                elif volba == 2:
                    print("Zvolil si pridanie hesla.")
                    logger.info("Password added")
                    input("====Stlac enter====")
                elif volba == 3:
                    print("Zvolil si zmazanie hesla")
                    logger.info("Password deleted")
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
            print("Logging out.")
            logger.info("Log out")
            conn.close()

        elif x != str(se.getMessage()):
            print("Nespravny kod")
            logger.info("Unsuccessful login")


    elif choice == 2:
        logger.info("Sign up chosen")

    else:
        print("Nespravna volba.")
        input("====Stlac enter====")

    clearscreen()
    firstScreen()
    try:
        choice = int(input("Zvol moznost:"))
    except:
        print("Nespravny input.")
        break
print("Exit.")
logger.info("Quit")
conn.close()

















#Print databazy
#for row in c.execute('SELECT * FROM users;'):
#    print(row)
