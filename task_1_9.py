a, b, c = map(float, input('Enter three numbers: ').split())

if a == b or b == c or a == c:
    print('Mean value does not exist')
else:
    mean_val = a
    if a < b < c or c < b < a:
        mean_val = b
    if a < c < b or b < c < a:
        mean_val = c
    print(f'Mean value is {mean_val}')
