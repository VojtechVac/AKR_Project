from Crypto.Cipher import DES3
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
from hashlib import md5
from base64 import b64encode, decode, encode
from base64 import b64decode
import json

encrypting = input(" 1. 3DES | 2. ChaCha20 ")
if (encrypting == '1'):  # 3DES

    while True:
        choice = input("1.Encrypt | 2.Decrypt | 3.Stop | 4.Print ")
        with open('vault.db', 'rb') as input_file:
            file_bytes = input_file.read()
        key = "abcd"
        key_hash = md5(key.encode('ascii')).digest()
        tdes_key = DES3.adjust_key_parity(key_hash)
        cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')
        if (choice == '1'):
            # Priting encrypted info
            new_file_bytes = cipher.encrypt(file_bytes)
            print('Encrypting..')
            # print(new_file_bytes)
            with open('vault.db', 'wb') as output:
                output.write(new_file_bytes)
        elif(choice == '2'):
            # Printing decrypted info
            new_file_bytes = cipher.decrypt(file_bytes)
            print('Decrypting..')
            # print(new_file_bytes)
            with open('vault.db', 'wb') as output:
                output.write(new_file_bytes)
        elif(choice == '4'):
            # Printing
            print(file_bytes)
        elif(choice == '3'):
            break
        else:
            print("--Wrong choice--")


elif (encrypting == '2'):  # ChaCha20
    def keyGen(key):
        while len(key) % 32 != 0:
            key = key + b'0'
        return key

    passw = input("Please enter password: ")
    key = keyGen(bytes(passw, 'utf-8'))

    with open('vault_chacha.db', 'rb') as input_file:
        file_bytes = input_file.read()

    while True:

        choice = input("1.Encrypt | 2.Decrypt | 3.Stop | 4.Print ")
        if(choice == '1'):  # ENCRYPT
            plaintext = file_bytes
            cipher = ChaCha20.new(key=key)
            ciphertext = cipher.encrypt(plaintext)
            nonce = cipher.nonce
            # nonce = b64encode(cipher.nonce).decode('utf-8')
            #----- For console output only ----#
            # ct = b64encode(ciphertext).decode('utf-8')
            # result = json.dumps({'nonce': nonce, 'ciphertext': ct})
            # print(f'Encrypted message: {result}') --> for printing in here
            print("encrypted")
            with open('vault_chacha.db', 'wb') as output:
                output.write(ciphertext)
            with open('nonce_chacha.txt', 'wb') as nonc:
                nonce = cipher.nonce
                nonc.write(nonce)
            output.close()
            nonc.close()
        elif(choice == '2'):  # DECRYPT
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
        elif(choice == '3'):
            break
        elif(choice == '4'):
            with open('vault_chacha.db', 'rb') as reading:
                print(reading.read())
