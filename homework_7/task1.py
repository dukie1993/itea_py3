'''
Написати три функції. Задача першої функції: отримання всіх чисел з рядка 
за допомогою регулярного виразу. Задача другої функції: пошук в тексті 
дати у форматі “дд-мм-рррр” за допомогою регулярного виразу. 
Задача третьої функції: Перевірка, чи в тексті присутні слова “Red”, “Green”, “Blue”, “Yellow”
'''

import re

def get_all_digits(a):
    digits = re.findall(r'\d', a)
    print(digits)

def date_search(a):
    found_date = re.findall(r'\d\d-\d\d-\d{4}', a)
    print(found_date)

def word_search(a):
    found_word_1 = re.findall(r'Red', a)
    print(found_word_1)
    found_word_2 = re.findall(r'Green', a)
    print(found_word_2)
    found_word_3 = re.findall(r'Blue', a)
    print(found_word_3)
    found_word_4 = re.findall(r'Yellow', a)
    print(found_word_4)

    # Спробував зробити циклом
    # words = []
    # for w in a:
    #     search_word = re.findall(r'Red', a)
    #     if "Red" in search_word:
    #         words.append(w)
    # print(words)


get_all_digits('qwerty12345asdf54321')
date_search('19-07-2323')
word_search("Red, Green, Blue, Yellow, Black")