'''
Написати програму, яка буде видаляти всі дублюючі дані зі словника
'''

dic1 = {
    1 :"one",
    2 :"two",
    3 :"three",
    4 :"four",
    4 :"four",
    5 :"qwerty"
}

result = {}

for each_element in dic1:
    for key, value in dic1.items():
        if value not in result.values():
            result[key] = value
print(result)
