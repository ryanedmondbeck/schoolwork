# Ryan Beck | MCS 425 | 9.27.18
#
#### RSA ###########################################################
#
# Bob chooses p and q, computes n = pq
# chooses an encryption exponent e s.t. gcd(e,(p-1)(q-1)) = 1
# sends e and n to Alice
#
# Alice encrypts her message to m < n
# Alice computes m^e (mod n) = c
# sends c to Bob
#
# Bob computes de == 1(mod (p-1)(q-1))
# 	rewritted as de = 1 + k*(p-1)(q-1) for some int k
# Bob obtains d thru extended euclidean algo
# Bob computes c^d(mod n) = orignal message
#
#####################################################################

# converts message to numbers
def convert_message_to_numbers(message):
	
	mlist_char = list(message)
	m_list_int = []

	# dealing with data types is a mess in python
	for i in range(len(mlist_char)):
		# print('char is: ', mlist_char[i])
		temp = mlist_char[i]
		num = int(ord(temp))
		num -= 96
		# print('num is: ', num)
		if num < 10:
			m_list_int.append(0)
			m_list_int.append(num)
		else:
			m_list_int.append(num)
	m_string_int = ''.join(str(i) for i in m_list_int)
	m_int = int(m_string_int)

	return m_int

#####################################################################
# these functions are for the modular exponentiation
# algorithm for finding m^e(mod n)
# allows Alice to encrypt message c

binary = []
m_squares = []
m_squares2 = []

# creates a list representing a in binary
def convert_to_binary(e):
	d = int(e / 2)
	r = e % 2
	binary.insert(0, r)
	if d != 0:
		convert_to_binary(d)

# modular exponentiation by repeated squaring
def repeated_squaring(m, n):
	m_squares.append(m)
	for i in range(len(binary)):
		m_squares.append((m_squares[i] * m_squares[i]) % n)

	for i in range(len(binary)):
		if binary[i] == 1:
			m_squares2.append(m_squares[i])

	p = 1
	for i in m_squares2:
		p = (p * i) % n
		# print(p)
	return p

# function computes m^e (mod n) = c
def encryption_algo(m, e, n):
	convert_to_binary(e)
	binary.reverse()
	c = repeated_squaring(m, n)	
	return c

#####################################################################
# dectryption algorithm Bob computes
# de == 1(mod (p-1)(q-1))

# finds x, y s.t. xa + yb = gcd(a, b)
quotients = []

# returns greatest common divisor of a and b
def gcd(a, b):

    if b > a: 
        temp = b
        b = a
        a = temp

    r = a % b
    q = int(a / b)
    quotients.append(q)

    if a != (q * b) + r:
        print('Error: try with different primes p, q')
        sys.exit()
    if r == 0:
        return(b)
    return gcd(b, r) 

def extended(a, b, g):
    x0 = 0
    x1 = 1
    for i in range(len(quotients) - 1):
        x2 = -quotients[i] * x1 + x0
        x0 = x1
        x1 = x2

    y0 = 1
    y1 = 0
    for i in range(len(quotients) - 1):
        y2 = -quotients[i] * y1 + y0
        y0 = y1
        y1 = y2

    if ((a * x2) + (b * y2)) == g:
        print('--- %d(%d) + %d(%d) = %d' % (a, x2, b, y2, g))
        return x2

    elif ((a * y2) + (b * x2)) == g:
        print('--- %d(%d) + %d(%d) = %d' % (a, y2, b, x2, g))
        return y2
    else:
    	print("error------ extended euclidean algorithm failed")
    	quit()

def compute_d(e, n):
	g = gcd(e, n)
	d = extended(e, n, g)
	d += n
	return d

#####################################################################
# Bob computes c^d(mod n) = orignal message
dbinary = []
dm_squares = []
dm_squares2 = []

# creates a list representing a in binary
def dconvert_to_binary(e):
	d = int(e / 2)
	r = e % 2
	dbinary.insert(0, r)
	if d != 0:
		dconvert_to_binary(d)

# modular exponentiation by repeated squaring
def drepeated_squaring(m, n):
	dm_squares.append(m)
	for i in range(len(dbinary)):
		dm_squares.append((dm_squares[i] * dm_squares[i]) % n)

	for i in range(len(dbinary)):
		if dbinary[i] == 1:
			dm_squares2.append(dm_squares[i])

	p = 1
	for i in dm_squares2:
		p = (p * i) % n
	return p

def decryption_algo(c, d, n):
	dconvert_to_binary(d)
	dbinary.reverse()
	dm = drepeated_squaring(c, n)
	return dm


#####################################################################

def main():

	# Bob chooses p and q to compute n
	p = int(input('Bob: Choose prime number p: '))
	q = int(input('Bob: Choose prime number q: '))
	n = p*q
	print('--- n is : %d ---' % n)
	e = 9007  #65537
	print('--- The public key e is: %d ---' % e)
	# Bob sends n and e to Alice

	print('--- Bob sends n and e to Alice ---')
	# Alice encryps a message m 
	message = input('Alice: Enter the message to send to Bob: ')
	m = convert_message_to_numbers(message)
	print('unecnrypted message: ', m)
	c = encryption_algo(m, e, n)
	print('--- Alice sends encrypted message c to Bob: %d ---' % c)
	
	# Bob computes d and decrypts message
	d = compute_d(e, n)
	print("--- d: %d ---" % d)
	dm = decryption_algo(c, d, n)
	print('--- decrypted message: %d ---' % dm)

main()
