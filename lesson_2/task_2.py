'''Користувач вводить число n. Вивести на екран різницю добутків чисел n+1 та n-1. Тобто якщо було введено число 5, то результат має бути 20. 
Тобто: 5+1 = 6; 5-1=4; 6*6 - 4*4 = 20.'''

n = int(input("Enter number: "))
pos_n = n + 1  
neg_n = n - 1 
result = (pos_n*pos_n)-(neg_n*neg_n) #вираховуємо різницю добутків чисел n+1 та n-1
print(result)