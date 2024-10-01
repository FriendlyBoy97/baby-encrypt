import hashlib
import os
import bcrypt

# Generating a salt
salt = os.urandom(16)

# Hashing a password with bcrypt
password = b'kingbee123'
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

# Verifying the password
if bcrypt.checkpw(password, hashed):
    print("Password matches!")
else:
    print("Incorrect password.")