import math
print("Решение квадратного уравнения типа: 3x**2 + 12x + 10 = 0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
 
discr = b ** 2 - 4 * a * c #вычисляем дискриминант по формуле
print(f"Дискриминант D = {discr:.2f}")
 
if discr > 0: #если True то уравнение имеет 2 корня
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print(f"x1 = {x1:.2f} \nx2 ={x2:.2f}")
    print(type(x1))
    print(type(x2))
elif discr == 0: #если True то уравнение имеет 1 корень
    x = -b / (2 * a)
    print(f"x = {x:.2f}")
    print(type(x))
else: #если True то уравнение не имеет корней
    print("Корней нет")