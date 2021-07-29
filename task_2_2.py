def show_even_odd_count(number):
    """Display count of even and odd digits in the number"""
    even_count = 0
    odd_count = 0
    while number != 0:
        digit = number % 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        number //= 10
    print(f'even_count: {even_count}')
    print(f'odd_count: {odd_count}')


if __name__ == '__main__':
    num = int(input('Enter a number: '))
    show_even_odd_count(num)
