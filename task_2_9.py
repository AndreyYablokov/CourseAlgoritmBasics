def sum_digits(number):
    """Calculates the sum of the digits of a number"""
    result = 0
    while number != 0:
        result += number % 10
        number //= 10
    return result


def show_max_sum_digit(numbers):
    """Shows the number with the maximum sum of digits"""
    sum_digit_max = 0
    num_sum_max = 0
    for number in numbers:
        num_sum_digit = sum_digits(number)
        if num_sum_digit > sum_digit_max:
            sum_digit_max = num_sum_digit
            num_sum_max = number

    print(f'Number with max sum of digits: {num_sum_max}, their sum of digits: {sum_digit_max}')


if __name__ == '__main__':
    nums = map(float, input('Enter numbers: ').split())
    show_max_sum_digit(nums)

