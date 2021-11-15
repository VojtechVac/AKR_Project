
print("Zadaj email: ")
mail = input()
password = getpass.getpass(prompt='Zadaj heslo:')
#Hash hesla
login = Login(mail, password)
login.hashPassword()

#Vlozenie mailu a hashu hesla do databazy cez preparedstatement
#c.execute("""INSERT INTO users ('mail', 'password') VALUES (?, ?);""", (mail, login.getHash()))
conn.commit()

#Posielanie mailu, DOCASNE VYPNUTE
#se = sendEmail()
#se.send_email(mail) 
print("Zadaj kod:")
x = input()

if x == str(se.getMessage()):
    print("Spravny kod")
    logger.info("Successful login")
    input("====Stlač enter====")
    # MENU
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
    print("Exit.")
    logger.info("Quit")
    conn.close()

elif x != str(se.getMessage()):
    print("Nespravny kod")
    logger.info("Unsuccessful login")
