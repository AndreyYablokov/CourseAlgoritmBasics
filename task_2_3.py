def reverse_number_str(number):
    """Generates a number in which the digits are arranged in reverse order.
        The argument type is a string"""
    return number[::-1]


def reverse_number_dig_v1(number):
    """Generates a number in which the digits are arranged in reverse order.
        The argument type is an integer"""
    digits = []
    while number != 0:
        digits.append(number % 10)
        number //= 10
    idx = len(digits) - 1
    result = 0
    for digit in digits:
        result = result + digit * (10 ** idx)
        idx = idx - 1
    return result


def reverse_number_dig_v2(number):
    """Generates a number in which the digits are arranged in reverse order.
        The argument type is an integer"""
    count_digits = 0
    number_clone = number
    while number_clone != 0:
        count_digits = count_digits + 1
        number_clone //= 10
    idx = count_digits - 1
    result = 0
    while number != 0:
        digit = number % 10
        result += digit * (10 ** idx)
        idx = idx - 1
        number //= 10
    return result


if __name__ == '__main__':
    num = input('Enter a number: ')
    print('-' * 150)
    print(reverse_number_str(num))
    print('-' * 150)
    print(reverse_number_dig_v1(int(num)))
    print('-' * 150)
    print(reverse_number_dig_v2(int(num)))

