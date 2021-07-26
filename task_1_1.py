num = int(input('Enter a three-digit integer number: '))

if num < 100 or num > 999:
    raise ValueError('Wrong number')

sum_digit = 0
prod_digit = 1

digit = num % 10
sum_digit += digit
prod_digit *= digit
num //= 10

digit = num % 10
sum_digit += digit
prod_digit *= digit
num //= 10

digit = num % 10
sum_digit += digit
prod_digit *= digit

print(f'Sum of digits is {sum_digit}')
print(f'Product of digits is {prod_digit}')

