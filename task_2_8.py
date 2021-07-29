# Determining the count of repetitions of a number in a sequence

# Solution when using a list
nums_count = int(input('Enter a count of numbers: '))
idx = 1
numbers = []
while idx <= nums_count:
    numbers.append(float(input(f'Enter number №{idx}: ')))
    idx += 1

num_search = float(input('Enter a number for counting: '))

num_count = 0
for number in numbers:
    if number == num_search:
        num_count += 1

print(f'Count number: {num_count}')

# Solution when entering numbers in one line
numbers_str = input('Enter numbers: ')
num_search = float(input('Enter a number for counting: '))
num_count = 0
for number in numbers_str.split():
    if num_search == float(number):
        num_count += 1

print(f'Count number: {num_count}')

# Solution without using lists and strings
nums_count = int(input('Enter a count of numbers: '))
num_search = float(input('Enter a number for counting: '))
idx = 1
num_count = 0
while idx <= nums_count:
    number = float(input(f'Enter number №{idx}: '))
    if num_search == float(number):
        num_count += 1
    idx += 1

print(f'Count number: {num_count}')
