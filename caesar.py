# Caesar Cipher
# Ryan Beck | rbeck3 | September 3, 2018 | MCS 425 | Homework 1
# Code from inventwithpython.com has been referenced

MAX_KEY_SIZE = 26

############################################################################
# input functions

# determines if encryption of decryption will take place
def get_mode():
	while True:
		print('Do you wish to encrypt or decrypt a message?')
		mode = input().lower()
		if mode in ['encrypt', 'e', 'decrypt', 'd']:
			return mode
		else:
			print('Enter either "encrypt" or "e" or "decrypt" or "d".')

# user enters message into string
def get_message():
	print('Enter your message:')
	return input()

# user enters key length between 1-26
def get_key():
	key = 0
	while True:
		print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
		key = int(input())
		if (key >= 1 and key <= MAX_KEY_SIZE):
			return key

############################################################################
# encryption functions - you can see that it's less elegantly written
# than the decryption code because I was learning Python syntax as I went

# removes all characters that are not letters
def remove_nonletters(mode, message):
	# strings are immutable in python so must move to array first
	array_message = []
	if mode[0] == 'e':
		for symbol in message:
				if symbol.isalpha():
					array_message.append(symbol)
	new_message = ''.join(array_message)
	return new_message

# encryption helper function
def convert_to_nums(message):
	num_array = []
	for symbol in message:
		if symbol.islower():
			num = ord(symbol)
			# 'a' is 32 away from 'A
			num -= 32
			# converts from upercase ASCII to 0 - 25
			num -= 65
			num_array.append(num)
		elif symbol.isupper():
			num = ord(symbol)
			num -=65
			num_array.append(num)
	return num_array

# this is where the magic happens
def cipher(num_array, key):
	for i in range(len(num_array)):
		#equation for shift cipher!!!
		num_array[i] = (num_array[i] + key) % 26
		#convert back to uppercase ASCII
		num_array[i] = num_array[i] + 65
		#convert back to letters
		num_array[i] = chr(num_array[i])
	#create string
	ciphertext = ''.join(num_array)
	return ciphertext

def encrypt(message, key):
	message = remove_nonletters(mode, message)
	num_array = []
	num_array = convert_to_nums(message)
	message = cipher(num_array, key)
	return message

############################################################################
# decryption functions

def decrypt(ciphertext, key):
	# convert string to array
	char_array = list(ciphertext)
	for i in range(len(char_array)):
		#converts to ASCII numbers
		char_array[i] = ord(char_array[i])
		# converts from 0 - 25 to 65
		char_array[i] = char_array[i] - 65
		# shift cipher decryption formula
		char_array[i] = (char_array[i] - key) % 26
		#convert back to ASCII values
		char_array[i] = char_array[i] + 65
		#convert back to letters
		char_array[i] = chr(char_array[i])
	#create string
	plaintext = ''.join(char_array)
	return plaintext

############################################################################
# main

mode = get_mode()
message = get_message()
key = get_key()
if mode[0] == 'e':
	message = encrypt(message, key)
elif mode[0] == 'd':
	message = decrypt(message, key)
print('Your translated text is:')
print(message)