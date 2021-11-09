from email_pokus import sendEmail

print("vlož email: ")
se = sendEmail()
se.send_email(input()) 
print("Zadaj kód:")
x = input()

if x == str(se.getMessage()):
    print("Správny kód")
elif x != str(se.getMessage()):
    print("Nesprávny kód")
