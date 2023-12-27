def vigenere_encrypt(text, key):
    encrypted_text = ""
    key_length = len(key)
    
    for i, char in enumerate(text):
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.lower()) - ord('a')
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    
    return encrypted_text


text = "Hello, World!"
key = "KEY"

encrypted_text = vigenere_encrypt(text, key)
print("Зашифрованный текст:", encrypted_text)
