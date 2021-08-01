# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу

user_matrix = []
for idx in range(4):
    numbers_str = input(f'Enter 4 elements of matrix (row №{idx+1}): ').split()
    user_matrix.append([int(item) for item in numbers_str])
    user_matrix[idx].append(sum(user_matrix[idx]))

print('Result:')
for row in user_matrix:
    print(row)
