'''
Створити програму, яка об’єднуватиме інформацію з двох файлів у один. 
Тобто користувач має ввести ім’я першого файлу, ім’я другого файлу для зчитування і 
ім’я третього файлу, в який буде об’єднано 2 попередні.
'''

file1 = open(input("Enter 1 file path: "), "r").read()
file2 = open(input("Enter 2 file path: "), "r").read()
file3 = open(input("Enter output file path: "), "w")
file3.write(file1 + "\n" + file2)
file3.close()