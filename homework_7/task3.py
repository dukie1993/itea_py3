'''
Реалізувати шифр Віженера.
'''
from time import sleep
alphabet = ' abcdefghijklmnopqrstuvwxyz'

def main():
	for_crypt = input("Enter text: ")
	key_encrypt = input("Enter key: ")

	# робимо ключ такої самої довжини як і слово
	while len(key_encrypt) < len(for_crypt):
		key_encrypt += key_encrypt
	key_encrypt = key_encrypt[:len(for_crypt)]

	# вибір дії над словом
	choose = int(input("Encode (1) or decode(2)?: "))
	# якщо 1 - зашифрувати
	if choose == 1:
		print(encrypt(for_crypt, key_encrypt)) 
	# якщо 2 - розшифрувати
	elif choose == 2:
		print(decrypt(for_crypt, key_encrypt))
	# завершення програми 
	else:
		print("Nothing to do. Exiting...")
		sleep(1)
		exit()

# шифруємо текст 
def encrypt(text, key): # a = слово яке треба зашифрувати, b = слово ключ
		
	encrypt_text = str()
	
	for i, letter in enumerate(text):
		index = alphabet.index(letter)
		key_index = alphabet.index(key[i % len(key)])
		index = (index + key_index) % len(alphabet)
		encrypt_text += alphabet[index]

	return encrypt_text

# розшифровуємо текст
def decrypt(text, key): # a = слово яке треба розшифрувати, b = слово ключ
	
	decrypted = str()
	
	for i, letter in enumerate(text):
		key_sym_index = alphabet.find(key[i])
		char_line = alphabet[key_sym_index:] + alphabet[:key_sym_index]
		decrypt_sym_index = char_line.find(text[i])
		ready_symbol = alphabet[decrypt_sym_index]
		decrypted += ready_symbol
		
	return decrypted


if __name__ == "__main__":
	main()