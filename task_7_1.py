# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в
# виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random
import cProfile


def bubble_sort_v1(massive):
    length_massive = len(massive)
    for dim in range(length_massive - 1):
        for idx in range(length_massive - dim - 1):
            if massive[idx] < massive[idx + 1]:
                massive[idx], massive[idx + 1] = massive[idx + 1], massive[idx]


def bubble_sort_v2(massive):
    length_massive = len(massive)
    for dim in range(length_massive - 1):
        need_sort = False
        for idx in range(length_massive - dim - 1):
            if massive[idx] < massive[idx + 1]:
                massive[idx], massive[idx + 1] = massive[idx + 1], massive[idx]
                need_sort = True
        if not need_sort:
            break


if __name__ == '__main__':
    massive_for_sort = [random.randint(-100, 100) for _ in range(10000)]
    print(massive_for_sort)
    bubble_sort_v2(massive_for_sort)
    print(massive_for_sort)

    massive_for_sort_1 = massive_for_sort.copy()
    massive_for_sort_2 = massive_for_sort.copy()
    cProfile.run('bubble_sort_v1(massive_for_sort_1)')
    cProfile.run('bubble_sort_v2(massive_for_sort_2)')

# Count of elements: 10000
# bubble_sort_v1 -> 4.262 seconds
# bubble_sort_v2 -> 0.001 seconds
