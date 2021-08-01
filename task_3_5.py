# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве

numbers_str = input('Enter elements of massive: ').split()
numbers = [int(item) for item in numbers_str]
max_negative_idx = 0
max_negative_num = min(numbers)
for idx, number in enumerate(numbers):
    if 0 > number > max_negative_num:
        max_negative_num = number
        max_negative_idx = idx

if max_negative_num >= 0:
    print('There is not negative numbers')
else:
    print(f'Max negative number: {max_negative_num} (idx = {max_negative_idx})')
