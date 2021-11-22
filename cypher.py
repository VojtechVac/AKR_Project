from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from hashlib import md5

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
        print(new_file_bytes)
    elif(choice == '3'):
        break
    else:
        print("Wrong choice")

    with open('vault.db', 'wb') as output_file:
        output_file.write(new_file_bytes)

input_file.close()
output_file.close()
