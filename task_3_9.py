# Найти максимальный элемент среди минимальных элементов столбцов матрицы

rows_num = int(input('Enter rows number: '))
user_matrix = []
for idx in range(rows_num):
    numbers_str = input(f'Enter elements of matrix (row №{idx+1}): ').split()
    user_matrix.append([int(item) for item in numbers_str])
    if idx == 0:
        min_num_matrix = list(user_matrix[idx])  # Copy list user_matrix[idx]
        columns_num = len(user_matrix[idx])
    else:
        if columns_num != len(user_matrix[idx]):
            print('Different number of items in rows')
            break
        idx_min = 0
        for min_num, number in zip(min_num_matrix, user_matrix[idx]):
            if number < min_num:
                min_num_matrix[idx_min] = user_matrix[idx][idx_min]
            idx_min += 1

max_num_among_min = min_num_matrix[0]
for item in min_num_matrix:
    if item > max_num_among_min:
        max_num_among_min = item

print('Minimum values in columns: ', *min_num_matrix)
print(f'Result (maximum among minimum values in columns): {max_num_among_min}')
