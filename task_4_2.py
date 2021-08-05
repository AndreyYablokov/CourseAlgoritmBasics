# Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»

import cProfile


def eratosthenes_sieve(numbers):
    numbers[1] = 0
    max_number = len(numbers)
    for idx in range(max_number):
        if numbers[idx] != 0:
            for idx_not_prime_num in range(idx * 2, max_number, idx):
                numbers[idx_not_prime_num] = 0

    result = []
    for number in numbers:
        if number != 0:
            result.append(number)

    return result


def prime_numbers_ver1(numbers):
    result = []
    for number in numbers:
        flag_prime_number = True
        for divider in range(2, int(number/2)+1):
            if number % divider == 0:
                flag_prime_number = False
                break
        if flag_prime_number:
            result.append(number)

    return result


def prime_numbers_ver2(numbers):
    result = []
    for number in numbers:
        flag = True
        for divider in range(2, int(pow(number, 0.5))+1):
            if number % divider == 0:
                flag = False
                break
        if flag:
            result.append(number)

    return result


def prime_numbers_ver3(numbers):
    result = []
    for number in numbers:
        flag = True
        if number % 2 == 0:
            flag = False
        else:
            for divider in range(3, int(pow(number, 0.5))+1, 2):
                if number % divider == 0:
                    flag = False
                    break
        if flag or number == 2:
            result.append(number)

    return result


if __name__ == '__main__':
    nums = [idx for idx in range(0, 1000000)]

    print(eratosthenes_sieve(nums[::1]))
    print(prime_numbers_ver1(nums[2::1]))
    print(prime_numbers_ver2(nums[2::1]))
    print(prime_numbers_ver3(nums[2::1]))

    cProfile.run('eratosthenes_sieve(nums)')
    cProfile.run('prime_numbers_ver1(nums)')
    cProfile.run('prime_numbers_ver2(nums)')
    cProfile.run('prime_numbers_ver3(nums)')

# Результаты cProfile:
# num     | eratosthenes_sieve | prime_numbers_ver1 | prime_numbers_ver2 | prime_numbers_ver3 |
# 1000000 | 0.373 seconds      | -                  | 3.620 seconds      | 1.913 seconds      |
# 100000  | 0.031 seconds      | 13.878 seconds     | 0.157 seconds      | 0.055 seconds      |
# 10000   | 0.003 seconds      | 0.185 seconds      | 0.011 seconds      | 0.003 seconds      |
