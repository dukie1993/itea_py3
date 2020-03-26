'''
Написати програму, яка рахуватиме кількість кожного слова у файлі. Використовувати словники.
'''

words = "слово1 слово2 слово1 слово3 слово2 Вася слово1 Петя Вася Миша Вася Привет слово2"
word_list = words.split()

from collections import defaultdict
word_count_dict = defaultdict(int)

for word in word_list:
    print(word, word_count_dict[word])
    word_count_dict[word] += 1



some_text = "слово1 слово2 слово1 слово3 слово2 Вася слово1 Петя Вася Миша Вася Привет слово2"
words = some_text.split(' ')
 
words_counter = {}
for word in words:
    if word in words_counter:
        words_counter[word] += 1
    else:
        words_counter[word] = 1
 
print(words_counter)