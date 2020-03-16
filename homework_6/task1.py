'''
Написати програму, яка генеруватиме пароль. Пароль генерується рандомно, може 
включати лише букви(верхнього і нижнього регістру). Користувач може вказати довжину 
пароля. Якщо пароль користувачеві не сподобався, перегенеровувати його, доки йому сподобається. 
Програму розбити на функції.
'''

import string
from time import sleep
from random import *
def password_generator(a=8):
    try:
        a = int(a)
        if a == 0:
            print("Ви ввели 0, повторіть спробу.")
            password_generator(input("Введіть бажану кількість символів: "))
        while a > 0:
            characters = string.ascii_letters + string.punctuation  + string.digits
            password =  "".join(choice(characters) for x in range(a))
            print("Ваший пароль:", password)
            repeat = input("Бажаєте повторити генерацію? - Y/N: ").lower()
            if repeat == "y":
                print("Повторна генерація...")
                sleep(1)
                password_generator(input("Введіть бажану кількість символів: "))
            elif repeat == "n":
                print("Завершення програми.")
                exit()
            break
    except ValueError:
        print("Повторіть введення, очікується цифра.")
        password_generator(input("Введіть бажану кількість символів: "))

password_generator(input("Введіть бажану кількість символів: "))
