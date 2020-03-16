'''
Користувач вводить строку і пошукове слово. Вивести на екран, 
скільки разів пошукове слово зустрічається в строці. 
Регістр не враховувати
'''

import re
a = 'In a hole in the ground there lived a ground like at the 5-th stars ground'
res = len(re.findall(r'\b{}\b'.format(input()), a))
print(res)