print('''Конвертер валют на Python
Підтримує долари(USD), євро(EUR) та гривні(UAH)
''')
try:
    amount = float(input("Яку сумму хочеш конвертувати?\nСумма - "))
except ValueError:
    print("Введена сума має бути числом.")
    exit()
try:
    currency = int(input("Яка це валюта? 1 - USD, 2 - EUR, 3 - UAH\nВалюта - "))
    if not 1 <= currency <= 3:
        raise ValueError("Ви ввели вхідну валюту, яка поки що не підтримується. ;)")
    choose_currency = int(input("У яку валюту перевести? 1 - USD, 2 - EUR, 3 - UAH\nПеревести у - "))
    if not 1 <= choose_currency <= 3:
        raise ValueError("Ви ввели вихідну валюту, яка поки що не підтримується. ;)")
except ValueError as e:
    print("Не можу обробити дані.", e)
    exit()

#тіло програми
if currency == 1 and choose_currency == 2:
    result = round((amount / 1.1), 2)
    cur1, cur2 = "USD", "EUR"
elif currency == 1 and choose_currency == 3:
    result = round((amount * 24), 2)
    cur1, cur2 = "USD", "UAH"
elif currency == 2 and choose_currency == 1:
    result = round((amount * 1.1), 2)
    cur1, cur2 = "EUR", "USD"
elif currency == 2 and choose_currency == 3:
    result = round((amount * 27), 2)
    cur1, cur2 = "EUR", "UAH"
elif currency == 3 and choose_currency == 1:
    result = round((amount / 24), 2)
    cur1, cur2 = "UAH", "USD"
elif currency == 3 and choose_currency == 2:
    result = round((amount / 27), 2)
    cur1, cur2 = "UAH", "EUR"
else:
    print(f"Відсутні дані для конвертування, {amount} is {amount}")
    exit()
print(f"\n{amount} {cur1} = {result} {cur2}")
