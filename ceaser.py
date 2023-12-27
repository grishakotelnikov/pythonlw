def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text



text = input("Введите текст " )
shift = input("Введите сдвиг ")

encrypted_text = caesar_encrypt(text, int(shift))
print("Зашифрованный текст:", encrypted_text)


