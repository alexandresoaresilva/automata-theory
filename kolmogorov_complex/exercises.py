#exercises from Kolmogorov complexity, theory of Automata at Texas Tech

# 1. a hundred 1's in a row
# print("1\n"*100)
# 2. 101010... (a  thousand bits)
# print("1\n0"*1000)
# 3. 1011001010101100101101001101 OR 10 1100 101010 1100 10 1101 00 1101

# 4. 1001001
# print('1\n0\n0\n'*2 + '1')
# 5. 001001001... (a hundred bits)
# print('0\n' +'0\n1\n0\n'*33)
# 6. 100100100... (a thousand bits)
# print(len('100'*333+'1'))
# print('1\n0\n0\n'*333 + '1')
# 7. 011010100010100010100010000010... (ten thousand bits)
    print('0\n1\n1\n0')
    x = 20
    for i in range(0,5):
        x = x >> i
        y = bin(x)
        for j in range(0,len(y)):
            if y[j] == 'b':
                j = j + 1
            else:
                print(y[j])

# 	# hint: x(n) is 1 iff n is prime.
#
# 8. 011111011111011111... (500 bits)

for i in range(0,500):
    print('0\n'+'1\n'*5)
# 9. 101010... (forever)
# 10. 101001000100001... (forever)

