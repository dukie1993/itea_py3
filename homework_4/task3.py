# програміст 13 бухгалтер 10 офіціант 7 інші 5
calary = int(input("Введіть вашу зарплату: - "))
post = input("Введіть вашу посаду: ").lower()
if post == "програміст":
    tax = round((calary * 0.13), 2)
elif post == "бухгалтер":
    tax = round((calary * 0.1), 2)
elif post == "офіціант":
    tax = round((calary * 0.07), 2)
else: # post != strings 4,7,10
    tax = round((calary * 0.05), 2)
print(f'\n\x1b[1;31mВам необхідно заплатити {tax} грн. податків.')