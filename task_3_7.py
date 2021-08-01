# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться

numbers_str = input('Enter elements of massive: ').split()
numbers = [int(item) for item in numbers_str]
min_nums = [numbers[0], numbers[1]]
for number in numbers:
    if number < min_nums[0]:
        min_nums[0] = number
    elif number < min_nums[1]:
        min_nums[1] = number

print('Min values:', *min_nums)
