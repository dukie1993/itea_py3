'''
Реалізувати шифр Віженера. Не списувати :)
'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'
 
text = 'message'
key = 'word'
 
encrypt_text = str()
 
for i, letter in enumerate(text):
	index = alphabet.index(letter)
 
	key_index = alphabet.index(key[i % len(key)])
 
	index = (index + key_index) % len(alphabet)
	encrypt_text += alphabet[index]
 
print(encrypt_text)