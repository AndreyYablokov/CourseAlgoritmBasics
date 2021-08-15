# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
# называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках

import random
import cProfile


def quick_select(massive, idx):
    if len(massive) == 1:
        return massive[0]
    elements_lows = []
    elements_highs = []
    elements_equal = []
    base_elem = random.choice(massive)
    for elem in massive:
        if elem == base_elem:
            elements_equal.append(elem)
        elif elem < base_elem:
            elements_lows.append(elem)
        else:
            elements_highs.append(elem)
    if idx < len(elements_lows):
        return quick_select(elements_lows, idx)
    elif idx < len(elements_lows) + len(elements_equal):
        return base_elem
    else:
        return quick_select(elements_highs, idx - len(elements_lows) - len(elements_equal))


def median_massive_v1(massive):
    length_massive = len(massive)
    if length_massive % 2 == 0:
        return 0.5 * (quick_select(massive, length_massive / 2 - 1) +
                      quick_select(massive, length_massive / 2))
    else:
        return quick_select(massive, length_massive / 2)


def heap_sort(massive):
    length_massive = len(massive)

    for idx in range(length_massive, -1, -1):
        max_heap(massive, length_massive, idx)

    for idx in range(length_massive-1, 0, -1):
        massive[idx], massive[0] = massive[0], massive[idx]
        max_heap(massive, idx, 0)


def max_heap(massive, length_massive, idx_element):
    idx_left_element = 2 * idx_element + 1
    idx_right_element = 2 * idx_element + 2

    idx_largest_element = idx_element
    if idx_left_element < length_massive and massive[idx_largest_element] < massive[idx_left_element]:
        idx_largest_element = idx_left_element
    if idx_right_element < length_massive and massive[idx_largest_element] < massive[idx_right_element]:
        idx_largest_element = idx_right_element

    if idx_largest_element != idx_element:
        massive[idx_element], massive[idx_largest_element] = massive[idx_largest_element], massive[idx_element]
        max_heap(massive, length_massive, idx_largest_element)


def median_massive_v2(massive):
    copy_massive = massive.copy()
    heap_sort(copy_massive)
    return copy_massive[int(len(copy_massive)/2)]


if __name__ == '__main__':
    num = 100000
    massive_length = 2 * num + 1
    massive_init = [random.randint(0, 100) for _ in range(massive_length)]
    print(median_massive_v1(massive_init))
    print(median_massive_v2(massive_init))
    # cProfile.run('median_massive_v1(massive_init)')
    # cProfile.run('median_massive_v2(massive_init)')
    massive_init.sort()
    print(massive_init)

# Count of elements: 100000
# median_massive_v1 -> 0.164 seconds
# median_massive_v2 -> 2.392 seconds
