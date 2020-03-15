'''
Написати програму, яка генеруватиме пароль. Пароль генерується рандомно, може 
включати лише букви(верхнього і нижнього регістру). Користувач може вказати довжину 
пароля. Якщо пароль користувачеві не сподобався, перегенеровувати його, доки йому сподобається. 
Програму розбити на функції.
'''

import string
from random import *
def password_generator(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Incorrect input.")
        exit()
    characters = string.ascii_letters + string.punctuation  + string.digits
    password =  "".join(choice(characters) for x in range(a, b))
    print("Your password is:", password)

password_generator(8, 16)