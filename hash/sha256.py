import hashlib

def hash_password(password):
   # change the password to bytes
   password_bytes = password.encode('utf-8')

   # generate a SHA-256 hash object
   hash_object = hashlib.sha256()

   # update the hash object with the password bytes
   hash_object.update(password_bytes)

   # the hexadecimal representation of the hashed password
   hashed_password = hash_object.hexdigest()

   return hashed_password

# function execution
password = "kingbee123"
hashed_password = hash_password(password)
print("Hashed password:", hashed_password)