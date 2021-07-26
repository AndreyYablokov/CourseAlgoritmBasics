x1, y1 = map(float, input('Enter the coordinates of the first point separated by space: ').split())
x2, y2 = map(float, input('Enter the coordinates of the second point separated by space: ').split())

if x1 == x2 and y1 == y2:
    print('Result: this is one point')
elif x1 == x2:
    print('Result: y is independent of x')
elif y1 == y2:
    b = y1
    print(f'Result: y = {b:.5f}')
else:
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    sign_b = '+'
    if b < 0:
        sign_b = '-'
    print(f'Result: y = {k:.5f} * x {sign_b} {abs(b):.5f}')
