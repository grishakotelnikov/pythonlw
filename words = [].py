sentence = input("Введите предложение: ")

capitalized_sentence = ' '.join(word.capitalize() for word in sentence.split())

print("Предложение с заглавными буквами:")
print(capitalized_sentence)