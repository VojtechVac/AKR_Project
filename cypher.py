from Crypto.Cipher import DES3
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
from hashlib import md5
from base64 import b64encode
from base64 import b64decode
import json
youshallchoose = input("1. 3DES | 2. ChaCha20 :")
if (youshallchoose == 1):
    # 3DES
    while True:
        choice = input("1.Encrypt | 2.Decrypt | 3.Stop | 4. Print : ")
        with open('vault.db', 'rb') as input_file:
            file_bytes = input_file.read()
        key = "abcd"
        key_hash = md5(key.encode('ascii')).digest()
        tdes_key = DES3.adjust_key_parity(key_hash)
        cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b'0')
        if (choice == '1'):
            print('Encrypting..')
            new_file_bytes = cipher.encrypt(file_bytes)
        elif(choice == '2'):
            print('Decrypting..')
            new_file_bytes = cipher.decrypt(file_bytes)
        elif(choice == '4'):
            new_file_bytes = file_bytes
            print(new_file_bytes)
        elif(choice == '3'):
            break
        else:
            print("Wrong choice")
        with open('vault.db', 'wb') as output_file:
            output_file.write(new_file_bytes)

    input_file.close()
    output_file.close()
if(youshallchoose == 2):
    # ChaCha20
    # ENCODE
    def keyGen(key):
        while len(key) % 32 != 0:
            key = key + b'0'
        return key

    key = input("Please enter password: ")
    keyBytes = keyGen(bytes(key, 'utf-8'))

    with open('vault.db', 'rb') as input_file:
        file_bytes = input_file.read()

    # ENCODE
    plaintext = file_bytes
    cipher = ChaCha20.new(key=keyBytes)
    ciphertext = cipher.encrypt(plaintext)
    nonce = b64encode(cipher.nonce).decode('utf-8')
    ct = b64encode(ciphertext).decode('utf8')
    result = json.dumps({'nonce': nonce, 'ciphertext': ct})
    print(f'Encrypted message: {result}')
    # DECODE
    try:
        json_text = result
        b64 = json.loads(json_text)
        nonce = b64decode(b64['nonce'])
        ciphertext = b64decode(b64['ciphertext'])
        cipher = ChaCha20.new(key=keyBytes, nonce=nonce)
        backtext = cipher.decrypt(ciphertext)
        backtext = backtext.lstrip()
        print(f'Decrypted message: {backtext}')
    except ValueError or KeyError:
        print("Incorrect decryption")
