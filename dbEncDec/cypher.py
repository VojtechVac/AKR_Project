from Crypto.Cipher import DES3
from Crypto.Cipher import ChaCha20
from Crypto.Cipher import AES
from hashlib import md5
from base64 import b64encode, decode, encode
from base64 import b64decode
# from Crypto.Random import get_random_bytes # Není potřeba, použito pro testování
# import os                                   # Testování aktivní directory protože windows je na kokos

# import json
passw = input("Please enter password: ")
if(len(passw) != 0):
    encrypting = input(" 1. 3DES | 2. ChaCha20 | 3. AES ")
    #+-------- 3DES --------+#
    if (encrypting == '1'):
        while True:
            choice = input("1.Encrypt | 2.Decrypt | 3.Stop | 4.Print ")
            with open('vault.db', 'rb') as input_file:
                file_bytes = input_file.read()
            key = "abcd"
            key_hash = md5(key.encode('ascii')).digest()
            tdes_key = DES3.adjust_key_parity(key_hash)
            cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')
            # Encryption
            if (choice == '1'):
                new_file_bytes = cipher.encrypt(file_bytes)
                print('Encrypting..')
                with open('vault.db', 'wb') as output:
                    output.write(new_file_bytes)
            # Decryption
            elif(choice == '2'):
                new_file_bytes = cipher.decrypt(file_bytes)
                print('Decrypting..')
                with open('vault.db', 'wb') as output:
                    output.write(new_file_bytes)
            # Printing
            elif(choice == '4'):
                print(file_bytes)
            # Stop
            elif(choice == '3'):
                break
            else:
                print("--Wrong choice--")
    #+-------- ChaCha20 --------+#
    elif (encrypting == '2'):
        # Funkce pro generaci klíče
        def keyGen(key):
            while len(key) % 32 != 0:
                key = key + b'0'
            return key
        # Generování klíče
        key = keyGen(bytes(passw, 'utf-8'))

        # Načtení databáze do proměnné
        with open('vault_chacha.db', 'rb') as input_file:
            file_bytes = input_file.read()
        input_file.close()

        while True:
            choice = input("1.Encrypt | 2.Decrypt | 3.Stop | 4.Print ")
            # Encryption
            if(choice == '1'):
                plaintext = file_bytes
                cipher = ChaCha20.new(key=key)
                ciphertext = cipher.encrypt(plaintext)
                nonce = cipher.nonce
                #----- For console output only ----#
                # ct = b64encode(ciphertext).decode('utf-8')
                # result = json.dumps({'nonce': nonce, 'ciphertext': ct})
                # print(f'Encrypted message: {result}') --> for printing in here
                print("encrypted")
                with open('vault_chacha.db', 'wb') as output:
                    output.write(ciphertext)
                with open('nonce_chacha.txt', 'wb') as nonc:
                    nonc.write(nonce)

                output.close()
                nonc.close()
            # Decryption
            elif(choice == '2'):
                try:
                    with open('nonce_chacha.txt', 'rb') as nc:
                        nonce = nc.read()
                    with open('vault_chacha.db', 'rb')as ciphtext:
                        ciphertext = ciphtext.read()

                    cipher = ChaCha20.new(key=key, nonce=nonce)
                    dectext = cipher.decrypt(ciphertext)
                    print(cipher.nonce)
                    print("decrypted..")
                    with open('vault_chacha.db', 'wb') as dec:
                        dec.write(dectext)

                    nc.close()
                    ciphtext.close()
                    dec.close()
                except ValueError or KeyError:
                    print("Incorrect decryption")
            # Stop
            elif(choice == '3'):
                break
            # Print db
            elif(choice == '4'):
                with open('vault_chacha.db', 'rb') as reading:
                    print(reading.read())
    #+-------- AES --------+#
    elif(encrypting == '3'):

        # Funkce pro tvorbu klíče
        def keyGen(passw, size):
            while len(passw) % size != 0:
                passw = passw + b'0'
            return passw

        # Generování klíče 16 nebo 32 Bytes
        keySize = input("Vyberte délku klíče: (16B | 32B): ")
        if(keySize == '16' or keySize == '32'):
            keySize = int(keySize)
            key = keyGen(bytes(passw, 'utf-8'), keySize)
        else:
            print("Špatná délka")

        # IV lebože AES library mě nemá ráda
        iv = "This is an IV456"

        # Loop pro testování
        while True:
            choice = input(" 1.Encrypt | 2.Decrypt | 3.Stop | 4.Print : ")
            # Encryption
            if(choice == '1'):
                # def encryption():
                cipher = AES.new(key, AES.MODE_CBC, bytes(iv, 'utf-8'))

                with open('vault.db', 'rb') as f:
                    message = f.read()

                ciphertext = cipher.encrypt(message)

                with open('vault.db', 'wb') as e:
                    e.write(ciphertext)

            # Decryption
            elif(choice == '2'):
                # def decryption(self):
                cipher = AES.new(key, AES.MODE_CBC, bytes(iv, 'utf-8'))

                with open('vault.db', 'rb') as f:
                    ciphertext = f.read()

                message = cipher.decrypt(ciphertext)

                with open('vault.db', 'wb') as e:
                    e.write(message)
            # Stop
            elif(choice == '3'):
                break
            # Print db info
            elif(choice == '4'):
                with open('vault.db', 'rb') as f:
                    print(f.read())
            else:
                print("--Wrong choice--")
    else:
        print("--wrong choice--")

else:
    print("You need to enter a password")
