# Vigenere Cipher
# Ryan Beck | rbeck3 | September 3, 2018 | MCS 425 | Homework 1
############################################################################
# input functions

# determines if encryption of decryption will take place
def get_mode():
	while True:
		print('Do you wish to encrypt or decrypt a message?')
		mode = input().lower()
		if mode in ['encrypt', 'e', 'decrypt', 'd', 'unknown', 'u']:
			return mode
		else:
			print('Enter either "encrypt" or "e", "decrypt" or "d", "unknown" or "u".')

# user enters message into string
def get_message():
	print('Enter your message:')
	return input()

# user enters key length between 1-26
def get_key():
	key = ''
	while True:
		print('Enter the key, a string of letters, or a word:')
		key = input()
		return key

############################################################################
# encryption functions 

# removes all characters that are not letters
def remove_nonletters(message):
	# strings are immutable in python so must move to array first
	list_message = []
	for symbol in message:
		if symbol.isalpha():
			list_message.append(symbol)
	return list_message

# makes character into a number 0 - 25
def make_number(letter):
	# convert letter to ascii
	cipher_letter = ord(letter)
	# convert cipher letter to lowercase
	if letter.isupper():
		cipher_letter += 32
	cipher_letter -= 97
	return cipher_letter

# this is where the magic happens
def cipher(letter, key):
	cipher_letter = make_number(letter)
	cipher_key = make_number(key)
	# shift cipher formula
	cipher_letter = (cipher_letter + cipher_key) % 26
	return cipher_letter

# makes numbers 0 - 25 into lowercase ascii characters
def make_letter(number):
	number += 97
	letter = chr(number)
	return letter

# function for vigenere encryption
def encrypt(message, key):
	list_message = []
	list_ciphertext = []
	list_message = remove_nonletters(message)
	list_key = remove_nonletters(key)
	key_length = len(key)
	key_index = 0
	for x in range(len(list_message)):
		if key_index == (key_length):
			key_index = 0
		list_ciphertext.append(cipher(list_message[x], list_key[key_index]))
		key_index += 1
	string_ciphertext = []
	x = 0
	for x in range(len(list_ciphertext)):
		string_ciphertext.append(make_letter(list_ciphertext[x]))
	ciphertext = ''.join(string_ciphertext)
	return ciphertext


############################################################################
# decryption functions

def decipher(letter, key):
	cipher_letter = make_number(letter)
	cipher_key = make_number(key)
	# shift decipher formula
	plaintext_letter = (cipher_letter - cipher_key) % 26
	return plaintext_letter

def decrypt(message, key):
	list_ciphertext = []
	list_ciphertext = remove_nonletters(message)
	list_key = []
	list_key = remove_nonletters(key)
	key_length = len(key)
	list_plaintext = []
	key_index = 0
	for x in range(len(list_ciphertext)):
		if key_index == (key_length):
			key_index = 0
		list_plaintext.append(decipher(list_ciphertext[x], list_key[key_index]))
		key_index += 1
	string_plaintext = []
	for x in range(len(list_plaintext)):
		string_plaintext.append(make_letter(list_plaintext[x]))
	plaintext = ''.join(string_plaintext)

	return plaintext
############################################################################
# unknown key

# class Shifted_Cipher:
# 	def __init__(self, cipher_shift, num_collisions):
# 		self.cipher_shift = []
# 		self.num_collisions = 0

def shift(l):
	x = l.pop(0)
	l.append(x)
	return l

#find the key length
def decrypt_unknown(ciphertext):
	ciphertext_list = list(ciphertext)
	#make ciphertext_list into numbers
	for x in range(len(ciphertext_list)):
		ciphertext_list[x] = make_number(ciphertext_list[x])
	#shift cipher the and store shifted cipehers in list
	list_of_shifts = []
	l = ciphertext_list.copy()
	for x in range(len(ciphertext_list) - 1):
		l = shift(l)
		list_of_shifts.append(l.copy())
	# check for amount of collisions
	collision_counts = []
	for x in range(len(ciphertext_list) - 1):
		collision_counts.append(0)
		for y in range(len(ciphertext_list) - 1):
			if ciphertext_list[y] == list_of_shifts[x][y]:
				collision_counts[x] += 1
	print(collision_counts)
	# find index of most collisions
	
	max_index = collision_counts.index(max(collision_counts))
	
	# max_index = 0
	# for x in range(15):
	# 	# print(collision_counts[x])
	# 	if collision_counts[x] > max_index:
	# 		max_index = x
	# 	print('max_index ', max_index)
	
	print(max_index)

	return

############################################################################
# main

mode = get_mode()
message = get_message()
if mode[0] == 'e':
	key = get_key()
	message = encrypt(message, key)
elif mode[0] == 'd':
	key = get_key()
	message = decrypt(message, key)
elif mode[0] == 'u':
	message = decrypt_unknown(message)
print('Your translated text is:')
print(message)