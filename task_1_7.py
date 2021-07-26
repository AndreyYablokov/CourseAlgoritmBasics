a, b, c = map(float, input('Enter three numbers: ').split())

if a < b + c and b < a + c and c < a + b:
    if a == b and b == c:
        print('Equilateral triangle')
    elif a == b or b == c or a == c:
        print('Isosceles triangle')
    else:
        print('Versatile triangle')
else:
    print('Triangle does not exists')
