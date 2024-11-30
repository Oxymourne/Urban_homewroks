def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix


rows = int(input('Введите количество строк: '))
columns = int(input('Введите количество столбцов: '))
number = int(input('Введите элемент матрицы: '))

print(get_matrix(rows, columns, number))
