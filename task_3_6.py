# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать

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

# Variant 1
if min_idx < max_idx:
    sum_elems = sum(numbers[min_idx+1:max_idx])
else:
    sum_elems = sum(numbers[max_idx+1:min_idx])
print(f'Sum of elements between max and min numbers is {sum_elems}')

# Variant 2
sum_elems = 0
step = 1
if min_idx > max_idx:
    step = -1
for idx in range(min_idx + step, max_idx, step):
    sum_elems += numbers[idx]

print(f'Sum of elements between max and min numbers is {sum_elems}')
