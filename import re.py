import re


def check_password(password):
    if len(password) < 12:
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'[a-z]', password):
        return False
    
    if not re.search(r'[0-9]', password):
        return False
    
    if not re.search(r'[!@$%#^&*]', password):
        return False
    
    return True


password = input("Введите пароль: ")
if check_password(password):
    print("Пароль корректен.")
else:
    print("Пароль не соответствует требованиям.")
