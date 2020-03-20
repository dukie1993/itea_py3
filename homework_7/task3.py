'''
Реалізувати шифр Віженера. Не списувати :)
'''
def encrypt(a, b): # a = слово яке треба зашифрувати, b = слово ключ
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	
	encrypt_text = str()
	
	for i, letter in enumerate(a):
		index = alphabet.index(letter)
	
		key_index = alphabet.index(b[i % len(b)])
	
		index = (index + key_index) % len(alphabet)
		encrypt_text += alphabet[index]
	
	print(encrypt_text)


if __name__ == "__main__":
	encrypt("hello", "key")