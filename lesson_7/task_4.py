'''
Користувач вводить строку і пошукове слово. Вивести на екран, 
скільки разів пошукове слово зустрічається в строці. 
Регістр не враховувати
'''

string_1 = input("Строка: ").lower()
string_search = input("Пошукове слово: ").lower()
string_count = 0
while string_count >= len(string_1):
    if string_search in string_1:
        string_count += 1
        print(string_count)