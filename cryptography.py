from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes


class triDES:
    while True:
        try:
            key = DES3.adjust_key_parity(get_random_bytes(24))
            break
        except ValueError:
            pass

    # Encryption

    def encrypt(original_message):
        cipher = DES3.new(key, DES3.MODE_EAX)
        nonce = cipher.nonce
        encrypted_message = cipher.encrypt(original_message.encode('ascii'))
        return nonce, encrypted_message
    # Decryption

    def decrypt(nonce, ciphertext):
        cipher = DES3.new(key, DES3.MODE_EAX, nonce=nonce)
        decrypted_message = cipher.decrypt(ciphertext)
        return decrypted_message.decode('ascii')
