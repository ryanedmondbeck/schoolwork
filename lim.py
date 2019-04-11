
def main():
	n = 1
	m = 0.25
	c = 100
	while n > 0:
		n = n - m
		m = n * 0.25
		c -= 1
		print(n)

main()