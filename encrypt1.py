import base64

def xor_encrypt(plaintext, key):
    # Convert the plaintext into bytes
    plaintext_bytes = plaintext.encode()
    key_length = len(key)
    
    encrypted_bytes = bytearray()
    
    # XOR each byte of the plaintext with the key, repeating the key as needed
    for i in range(len(plaintext_bytes)):
        encrypted_byte = plaintext_bytes[i] ^ ord(key[i % key_length])
        encrypted_bytes.append(encrypted_byte)
    
    # Base64 encode the XORed result
    encrypted_base64 = base64.b64encode(encrypted_bytes).decode('utf-8')
    
    # Combine key with encrypted data for consistency with your code style
    return key + encrypted_base64

# Example usage:
key = "password"  # 8 characters (you can choose any key length)
plaintext = "Hello, Guy!"

encrypted_message = xor_encrypt(plaintext, key)
print("Encrypted message:", encrypted_message)