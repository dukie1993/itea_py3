try:
    week_num = input("Кількість тижнів: ")
    if week_num.isdigit():
        print(f"Ви обрали {week_num} тижнів.")
except ValueError as err:
    print("Невірний формат:", err, "- введені дані повинні бути числом.")