import random

def generate_omophonic_cipher():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    omophonic_cipher = {}

    for char in alphabet:
        replacements = [str(i) for i in range(1, random.randint(2, 5))]  
        omophonic_cipher[char] = replacements

    return omophonic_cipher

def encrypt_omophonic(text, omophonic_cipher):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            char = char.lower()  
            if char in omophonic_cipher:
                replacement = random.choice(omophonic_cipher[char])
                encrypted_text += replacement + " "
            else:
                encrypted_text += char + " "
        else:
            encrypted_text += char + " "

    return encrypted_text.strip()



text_to_encrypt = "Hello, World!"
omophonic_cipher = generate_omophonic_cipher()

encrypted_text = encrypt_omophonic(text_to_encrypt, omophonic_cipher)
print("Зашифрованный текст:", encrypted_text)
