# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

# Variant 1
numbers_str = input('Enter elements of massive: ').split()
numbers = [int(item) for item in numbers_str]
min_idx = 0
max_idx = 0
min_num = numbers[min_idx]
max_num = numbers[max_idx]
for idx, number in enumerate(numbers):
    if number < min_num:
        min_num = number
        min_idx = idx
    if number > max_num:
        max_num = number
        max_idx = idx

numbers[min_idx], numbers[max_idx] = numbers[max_idx], numbers[min_idx]

print('Result (variant 1): ', *numbers)

# Variant 2
numbers_str = input('Enter elements of massive: ').split()
numbers = [int(item) for item in numbers_str]
min_num = min(numbers)
max_num = max(numbers)
min_idx = []
max_idx = []
for idx, number in enumerate(numbers):
    if number == min_num:
        min_idx.append(idx)
    if number == max_num:
        max_idx.append(idx)

for item1, item2 in zip(min_idx, max_idx):
    numbers[item1], numbers[item2] = numbers[item2], numbers[item1]

print('Result (variant 2): ', *numbers)
