import numpy as np
import json

# Загрузка матрицы из файла
matrix = np.load('data/matrix_42.npy')

# Подсчет суммы и среднего арифметического всех элементов
total_sum = float(np.sum(matrix))
total_avr = float(np.mean(matrix))

# Подсчет суммы и среднего арифметического главной диагонали
sum_main_diag = float(np.trace(matrix))
avr_main_diag = float(np.trace(matrix) / matrix.shape[0])

# Подсчет суммы и среднего арифметического побочной диагонали
sum_sec_diag = float(np.trace(np.fliplr(matrix)))
avr_sec_diag = float(np.trace(np.fliplr(matrix)) / matrix.shape[0])

# Нахождение максимального и минимального значения
max_value = float(np.max(matrix))
min_value = float(np.min(matrix))

# Создание словаря с результатами
result = {
    'sum': total_sum,
    'avr': total_avr,
    'sumMD': sum_main_diag,
    'avrMD': avr_main_diag,
    'sumSD': sum_sec_diag,
    'avrSD': avr_sec_diag,
    'max': max_value,
    'min': min_value
}

# Запись результатов в JSON файл
with open('result.json', 'w') as json_file:
    json.dump(result, json_file)
