# Определить, какое число в массиве встречается чаще всего
import random
from pympler import tracker

tr = tracker.SummaryTracker()
numbers = [random.randint(0, 10000) for _ in range(1000000)]
uniq_numbers = set(numbers)
tr.print_diff()

# Вариант 1 (с использованием списка)
tr = tracker.SummaryTracker()
count_repetitions = [0] * len(uniq_numbers)
for number in numbers:
    for idx, uniq_number in enumerate(uniq_numbers):
        if number == uniq_number:
            count_repetitions[idx] += 1
            break

max_repetitions = max(count_repetitions)
print('-' * 150)
print('Variant 1')
print('-' * 150)
result = []
for idx, uniq_number in enumerate(uniq_numbers):
    if count_repetitions[idx] == max_repetitions:
        result.append(uniq_number)

print('Number with max repetitions: ', result[0])
tr.print_diff()

# Вариант 2 (с использованием словаря)
tr = tracker.SummaryTracker()
count_repetitions = {}
for number in numbers:
    if number not in count_repetitions:
        count_repetitions[number] = 1
    else:
        count_repetitions[number] += 1

print('-' * 150)
print('Variant 2')
print('-' * 150)
result = []
for key, value in count_repetitions.items():
    if value == max_repetitions:
        result.append(key)

print('Numbers with max repetitions: ', *result)
tr.print_diff()

# Расчет по формулам
# Расчет используемого объема памяти выполним при исходном массиве в 1 000 000 элементов, из них 10 000 уникальных чисел
# Python 3.8, OS x64
# Общий код
# Исходный список из 1 000 000 целый чисел: 24 * 1 000 000 (на целые числа) + 40 + 8 * 1 000 000 (список со ссылками) =
# = 32 000 040 байт = 30,5 МБ
# Множество для хранения 10 000 уникальных чисел: 24 * 10 000 (на целые числа) + 200 + 16 * 10 000 (множество со
# ссылками) = 400 200 байт = 0,4 МБ
# Вариант 1:
# Список с количеством повторений уникальных элементов: 24 * 10 000 (на целые числа) + 40 + 8 * 10 000 (список со
# ссылками) = 320 040 байт = 0,3 МБ
# Итого по варианту 1: 31,2 МБ
# Вариант 2:
# Словарь с количеством повторений уникальных элементов: 24 * 10 000 (на целые числа) + 248 + 24 * 10 000 (словарь со
# ссылками) = 480 248 байт = 0,5 МБ
# Итого по варианту 2: 31,4 МБ

# Результаты работы профилировщика по памяти
# Общий код:
# types |   # objects |   total size
# ===== | =========== | ============
#   int |      974508 |     26.02 MB
#  list |        2385 |      8.50 MB
#   set |           1 |    512.21 KB
# Вариант 1
# types |   # objects |   total size
# ====== | =========== | ============
#  list |           2 |     78.28 KB
# Вариант 2
# types |   # objects |   total size
# ===== | =========== | ============
#  dict |           2 |      288.84 KB
