# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9

numbers = [num for num in range(2, 10)]
multiplicity = [0] * len(numbers)

for item in range(2, 100):
    for idx, number in enumerate(numbers):
        if item % number == 0:
            multiplicity[idx] += 1

for idx, item in enumerate(multiplicity):
    print(f'Count numbers multiple of {numbers[idx]}: {item}')

print(f'Sum: {sum(multiplicity)}')
