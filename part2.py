import numpy as np

# Загрузка матрицы из файла
matrix = np.load('data/matrix_42_2.npy')

# Условие для отбора значений
condition = matrix > 542

# Создание массивов с индексами и значениями
indices_1, indices_2 = np.where(condition)
values_3 = matrix[condition]

# Сохранение массивов в файл формата npz
np.savez('result_arrays.npz', indices_1=indices_1, indices_2=indices_2, values_3=values_3)

# Сравнение размеров файлов
size_before = matrix.nbytes
size_after = sum(arr.nbytes for arr in [indices_1, indices_2, values_3])

print(f"Размер исходной матрицы: {size_before} байт")
print(f"Размер полученных массивов: {size_after} байт")

# Сохранение массивов в сжатом формате npz
np.savez_compressed('result_arrays_compressed.npz', indices_1=indices_1, indices_2=indices_2, values_3=values_3)

# Сравнение размеров сжатых файлов
size_after_compressed = sum(arr.nbytes for arr in np.load('result_arrays_compressed.npz').values())

print(f"Размер полученных массивов (сжатый формат): {size_after_compressed} байт")
