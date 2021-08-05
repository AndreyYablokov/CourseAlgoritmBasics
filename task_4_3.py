# В одномерном массиве целых чисел определить наименьший элемент

import cProfile
import random


def variant_with_for(numbers):
    min_nums = numbers[0]
    for number in numbers:
        if number < min_nums:
            min_nums = number

    return min_nums


def variant_with_builtin_funcs(numbers):
    return min(numbers)


if __name__ == '__main__':
    nums = [random.randint(0, 10000000) for _ in range(10000000)]
    cProfile.run('variant_with_for(nums)')
    cProfile.run('variant_with_builtin_funcs(nums)')

# Вариант функции с использованием цикла for -> 0.239
# Вариант функции с использованием встроенных функций -> 0.130
