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

get_all_digits('qwerty12345asdf54321')
date_search('19-07-2323')