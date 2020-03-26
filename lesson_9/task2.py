'''
Дано ось такий масив покупок. Вивести на екран загальну суму всіх покупок, 
а також утворити словник, де ключом виступає назва продукту, а значенням - загальна ціна за покупку.
'''

purchases = [
  {
    "name": "banana",
    "price_per_item": 100,
    "quantity": 3
  },
  {
    "name": "apple",
    "price_per_item": 5,
    "quantity": 8
  },
  {
    "name": "ice cream",
    "price_per_item": 150,
    "quantity": 4
  }
]

dic_2 = {}
summa = 0

for dict_purchases in purchases:
    summa += dict_purchases["quantity"] * dict_purchases["price_per_item"]
    dic_2[dict_purchases["name"]] = dict_purchases["price_per_item"] * dict_purchases["quantity"]

print(summa)
print(dic_2)