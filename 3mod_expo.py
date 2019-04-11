# algorithm for finding m^e(mod n)

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
	print(m_squares)

	for i in range(len(binary)):
		if binary[i] == 1:
			m_squares2.append(m_squares[i])
	print(m_squares2)

	p = 1
	for i in m_squares2:
		p = (p * i) % n
	print(p)

def main():
	# m = 30120
	# e = 9007
	# n = 211463707796206571

	m = 1418
	e = 13
	n = 2537

	convert_to_binary(e)
	binary.reverse()
	print('binary reverse: ', binary)
	repeated_squaring(m, n)	
	
main()