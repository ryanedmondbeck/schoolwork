# the extended Euclidean Algorithm
# used to compute x, y s.t. xa + yb = gcd(a, b)

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
        print('Error')
        sys.exit()

    if r == 0:
        return(b)

    return gcd(b, r)  

# prints x, y s.t. xa + yb = gcd(a, b)
def extended(a, b, g):

    x0 = 0
    x1 = 1
    for i in range(len(quotients) - 1):
        x2 = -quotients[i] * x1 + x0
        print(x2, x1, quotients[i], x0)
        x0 = x1
        x1 = x2

    y0 = 1
    y1 = 0
    for i in range(len(quotients) - 1):
        y2 = -quotients[i] * y1 + y0
        y0 = y1
        y1 = y2

    print('x, y s.t. xa + yb = gcd(a, b): ')
    if ((a * x2) + (b * y2)) == g:
        print('a: ', a, 'b: ', b, 'x: ', x2, 'y: ', y2, 'gcd(a, b): ', g)
        print('x, y s.t. %d(%d) + %d(%d) = %d' % (a, x2, b, y2, g))
    else:
        print('a: ', a, ', b: ', b, ', x: ', y2, ', y: ', x2, ', gcd(a, b): ', g)
        print('x, y s.t. %d(%d) + %d(%d) = %d' % (a, y2, b, x2, g))


def main():

    a = int(input('Enter integer a: '))
    b = int(input('Enter integer b: '))
    g = gcd(a, b)
    extended(a, b, g)

main()