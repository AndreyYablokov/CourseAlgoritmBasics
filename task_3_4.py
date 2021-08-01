# Определить, какое число в массиве встречается чаще всего

# Variant 1
numbers_str = input('Enter elements of massive: ').split()
numbers = [int(item) for item in numbers_str]
uniq_numbers = set(numbers)
count_repetitions = [0] * len(uniq_numbers)
for number in numbers:
    for idx, uniq_number in enumerate(uniq_numbers):
        if number == uniq_number:
            count_repetitions[idx] += 1
            break

max_repetitions = max(count_repetitions)
print('-'*150)
print('Variant 1')
print('-'*150)
result = []
for idx, uniq_number in enumerate(uniq_numbers):
    print(f'Count repetitions of number {uniq_number}: {count_repetitions[idx]}')
    if count_repetitions[idx] == max_repetitions:
        result.append(uniq_number)

print('Numbers with max repetitions: ', *result)

# Variant 2
count_repetitions = {}
for number in numbers:
    if number not in count_repetitions:
        count_repetitions[number] = 1
    else:
        count_repetitions[number] += 1

print('-'*150)
print('Variant 2')
print('-'*150)
result = []
for key, value in count_repetitions.items():
    print(f'Count repetitions of number {key}: {value}')
    if value == max_repetitions:
        result.append(key)

print('Numbers with max repetitions: ', *result)