'''
Користувач вказує дві назви файлів (у файлах якась текстова інформація). 
Після цього вказує, що знаходити спільне в даних файлах: речення, слова, 
словосполучення. Вивести на екран кількість спільних елементів, які запросив 
користувач.
'''
import colorama
from time import sleep

# * робота із першим файлом
file_for_compare_1 = open("data_test_1.txt", "r", encoding="utf-8") # * відкрити перший файл для порівняння
data_1 = file_for_compare_1.read() # * зчитую всю інформацію із data_test_1.txt
file_for_compare_1.close()

# * робота із другим файлом
file_for_compare_2 = open("data_test_2.txt", "r", encoding="utf-8") # * відкрити другий файл для порівняння
data_2 = file_for_compare_2.read() # * зчитую всю інформацію із data_test_2.txt
file_for_compare_2.close()

# ? Як зробити, щоб програма за замовчуванням вибирала варіант, але якщо треба, то користувач змінює це значення
print(colorama.Fore.GREEN +
    '''
File Comparator
Програма виводить кількість спільних елементів у двох файлах.

Що ви хочете шукати?

1: Слова
2: Словосполучення
3: Речення

0: Завершити программу
    '''
)
# standard_input = 1
user_choice = int(input("Зробіть свій вибір(1, 2, 3, 0): "))

if user_choice == 0:
    print('''Програма завершується.''')
    sleep(1.5)
    exit()

counter = 0
search_data = input("Введіть пошуковий запит: ")
while True:
    if user_choice == 1: # слово
        words_data_1 = data_1.split(" ")
        words_data_2 = data_2.split(" ")
        
        while True:
            if search_data in words_data_1 and words_data_2:
                counter += 1
                print(counter)
                index_1 = words_data_1.index(search_data)
                words_data_1 = words_data_1.pop(index_1)
                index_2 = words_data_2.index(search_data)
                words_data_2 = words_data_2.pop(index_2)
            else:
                break

    elif user_choice == 2: # словосполучення
        pass
        
    elif user_choice == 3: # речення
        pass
        
    else:
        print("Некоректне значення. Повторіть спробу.")
        continue
        
print(f'{counter} рази')

    