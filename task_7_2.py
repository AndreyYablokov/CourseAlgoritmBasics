# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(massive):
    length_massive = len(massive)
    if length_massive == 1:
        return massive
    length_new_massive = int(length_massive / 2)
    left_massive = merge_sort(massive[:length_new_massive])
    right_massive = merge_sort(massive[length_new_massive:])
    result = []

    length_left_massive = len(left_massive)
    length_right_massive = len(right_massive)
    idx_left = 0
    idx_right = 0
    while idx_left < length_left_massive and idx_right < length_right_massive:
        if left_massive[idx_left] <= right_massive[idx_right]:
            result.append(left_massive[idx_left])
            idx_left += 1
        else:
            result.append(right_massive[idx_right])
            idx_right += 1
    for idx in range(idx_left, length_left_massive):
        result.append(left_massive[idx])
    for idx in range(idx_right, length_right_massive):
        result.append(right_massive[idx])

    return result


if __name__ == '__main__':
    massive_for_sort = [random.uniform(0, 50) for _ in range(10)]
    print(massive_for_sort)
    sorted_massive = merge_sort(massive_for_sort)
    print(sorted_massive)

