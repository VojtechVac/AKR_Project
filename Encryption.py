from Crypto.Cipher import AES

class Encrypt:

    def encryption():
        cipher = AES.new("abcdefghijklmnof".encode("utf8"), AES.MODE_CBC, "ahojahojahojahoj".encode("utf8"))

        with open("users.db", "rb") as f:
            orig_file = f.read()

        def padFile(file):
            while len(file) % 16 != 0:
                file = file + b'0'
            return file

        padded_file = padFile(orig_file)

        encrypted_file = cipher.encrypt(padded_file)

        with open("users.db", "wb") as e:
            e.write(encrypted_file)

    def decryption(self):
        cipher = AES.new("abcdefghijklmnof".encode("utf8"), AES.MODE_CBC, "ahojahojahojahoj".encode("utf8"))

        with open("users.db", "rb") as f:
            encrypted_file = f.read()

        decrypted_file = cipher.decrypt(encrypted_file)

        with open("users.db", "wb") as e:
            e.write(decrypted_file)