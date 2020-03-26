'''
Користувач вводить рядок. Вивести на екран довжину найдовшого підрядка з даного рядка, 
в якому всі символи унікальні(тобто не повторюються). 
Наприклад: 
abcabcbb - Результат: 3 (“abc” - найдовший підрядок)
ccagrtfsdc - Результат: 8
aaa - Результат: 1
'''

some_text = input("Введіть деякий текст: ")
# some_text = "afdgetryfhgunfhd" - for AREPL in vs code

result = 0
substring = ""

for symbol in some_text:
    if symbol in substring:
        existing_symbol_index = substring.index(symbol) # індекс існуючого символу
        substring = substring[existing_symbol_index + 1:] + symbol # обрізає substring на +1 від індексу існуючого символу і додає новий символ
    else:
        substring += symbol
        result = max(result, len(substring)) # якщо substring > result тоді записує більше число в result

print(f"Довжина найдовшого підрядка: {result} символів.")
