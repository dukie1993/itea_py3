'''
Користувач вводить число. Після того, як було введено число, створити функцію-замикання, і 
передати число, яке ввів користувач. Далі запустити вічний цикл, всередині якого в користувача 
просити друге число, і використовуючи функцію-замикання, ділити дане число на те, яке ввів користувач спочатку.
'''

def add_numbers(n1):
    while True:
        def add_second_number(n2):
            return n2 // n1
        add_number2 = add_second_number(int(input("Enter second: ")))

    return add_second_number



add_number1 = add_numbers(int(input("Enter first: ")))
print(add_number1)



