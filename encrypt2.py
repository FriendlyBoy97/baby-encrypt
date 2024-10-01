import base64
import zlib

def encrypt(input_text):
    text = input_text.encode('utf-8')
    text = text[:-1]
    
    prefix = b"exec((_)(b'"  # Prefix: 11 'x' characters
    suffix = b"'))"   # Suffix: 3 'y' characters

    for i in range(50):
        # with open(f'output-{49-i}.txt', "w") as file:
        #     print(text.decode("utf-8"), file=file)
        # Add the prefix and suffix
        if not i == 0:
            text = prefix + text + suffix

        # Compress the text
        text = zlib.compress(text)
        
        # Base64 encode the text
        text = base64.b64encode(text)
        
        # Reverse the encoded text
        text = text[::-1]


    return text

# Example usage:
input_text = ""
with open("src.txt", 'r') as file:
    input_text = file.read()

encrypted_text = encrypt(input_text)
with open(f'output.txt', "w") as file:
    print(encrypted_text.decode("utf-8"), file=file)