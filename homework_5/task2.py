'''
Послідовність Фібоначчі. Користувач вводить число n. Вивести на екран перші n елементів 
послідовності фібоначчі. Тобто, якщо було введено число “6”, то на екрані має бути виведено 
“1, 1, 2, 3, 5, 8”.
'''

fib1 = fib2 = 1
 
n = int(input("Введіть номер елементу ряду Фібоначчі: "))
 
if n < 2:
    quit()
 
print(fib1, end=' ')
print(fib2, end=' ')
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')
print()
 