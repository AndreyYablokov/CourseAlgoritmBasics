# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться

import cProfile
import random


def variant_with_for(numbers):
    min_nums = [numbers[0], numbers[1]]
    for number in numbers:
        if number < min_nums[0]:
            min_nums[0] = number

    return min_nums


def variant_with_builtin_funcs(numbers):
    min_num_1 = min(numbers)
    idx_min_num_1 = numbers.index(min_num_1)
    min_num_2 = min(numbers[idx_min_num_1+1:])
    return [min_num_1, min_num_2]


if __name__ == '__main__':
    nums = [random.randint(0, 10000000) for _ in range(10000000)]
    cProfile.run('variant_with_for(nums)')
    cProfile.run('variant_with_builtin_funcs(nums)')

# Вариант функции с использованием цикла for -> 0.627
# Вариант функции с использованием встроенных функций -> 0.332
