"""
2.15 
Из данного предложения выбрать слова, имеющие заданное число букв.
"""

text = list(input("Введите текст: ").split())
word_len = int(input('Введите цифрой длину слов, которые следует найти в тексте: '))
print("Следующие слова соответсвуют заданным условиям:")
for word in text:
    formated_word = word.rstrip(',.!?:;')
    if len(formated_word) == word_len:
        print(formated_word)

