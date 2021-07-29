def check_theorem(number):
    """Checks the theorem 1+2+3+...+n = n * (n + 1) / 2"""
    sum_nums = 0
    for el in range(1, number + 1):
        sum_nums += el
    if sum_nums == number * (number + 1) / 2:
        return True
    else:
        return False


if __name__ == '__main__':
    num = int(input('Enter a number: '))
    for idx in range(1, num + 1):
        print(f'{idx} - {check_theorem(num)}')
