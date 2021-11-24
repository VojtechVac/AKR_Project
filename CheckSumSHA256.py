import hashlib

class CheckSum:

    def get_checksum(filename, hash_function):

        hash_function = hash_function
        filename = "users.db"

        with open(filename, "rb") as f:
            bytes = f.read()  # read file as bytes
            if hash_function == "sha256":
                readable_hash = hashlib.sha256(bytes).hexdigest()
            else:
                print("{} is an invalid hash function. Please Enter SHA256")
    
        return readable_hash

    path = "users.db"
    sha256_result = get_checksum(path, "sha256")
  
    print(str(sha256_result))