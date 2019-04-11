# hill cipher
# Ryan Beck | rbeck3 | September 12, 2018 | MCS 425 | Homework 2
###################################################################
from copy import copy, deepcopy

#------------------------------------------------------------------
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
		print('Enter your 9 digit key: ')
		key = input()
		return key
#------------------------------------------------------------------
# helper functions

# makes character into a number 0 - 25
def make_number(letter):
	# convert letter to ascii
	cipher_letter = ord(letter)
	# convert cipher letter to lowercase
	if letter.isupper():
		cipher_letter += 32
	cipher_letter -= 97
	
	return cipher_letter

# makes numbers 0 - 25 into lowercase ascii characters
def make_letter(number):
	number += 97
	letter = chr(number)
	return letter

def dot_product(V, M):
	dotprod = []
	for j in range(len(V)):
		sum =  0
		for i in range(len(M)):
			sum = sum + (V[i] * M[j][i])
		dotprod.append(sum)
	return dotprod

#------------------------------------------------------------------
#encryption
def split_list(l):
	print('l in split_list is: ', l)
	return l

def hillcipher(V, M):
	print('Vector V is: ', V)
	print('Matrix M is: ', M)
	
	dotprod = np.matmul(V, M)
	print('dotprod: ', dotprod)

	#take mod 26 
	for i in range(len(dotprod)):
		dotprod[i] %= 26
	print('dot product of V.M % 26 is: ', dotprod)
	
	#turn vector into letter vector
	for i in range(len(V)):
		letter = make_letter(V[i])

	return V

def encrypt(message, key):

	l = list(key)
	# make key list into Matrix M
	M = []
	x = 0
	for i in range(3):
		s = slice(x, x+3)
		M.append(l[s])
		x += 3
	# convert from 1 digit strings to integers
	for i in range(3):
		for j in range(3):
			M[i][j] = make_number(M[i][j])

	# make message into numbers
	m = list(message)
	for i in range(len(message)):
		num = make_number(m[i])
		m.pop(i)
		m.insert(i, num)
	
	# print('M in encrypt is: ', M)

	# find out how many 0's to add to end of m (ugly code)
	zeros = len(m) % 3
	if zeros == 1:
		m.append(0)
		m.append(0)
	if zeros == 2:
		m.append(0)

	print('m in encrypt is: ', m)
	length = len(m)
	lengthb = int(length/3)
	print(lengthb)
	m2 = []
	temp = []
	for i in range(lengthb):
		temp = split_list(m[i:i+3])
		print('temp in loop: ', i)
		m2.append(temp)
		i += 1
	print('m2: ', m2)

	# do the encryption
	# for i in range(len(m2)):
	# 	encrypted = hillcipher(m, M)
		

	return l
#------------------------------------------------------------------
# main
def main():
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

main()