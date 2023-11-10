import numpy as np
import json

matrix = np.load('../data/matrix_42.npy')

total_sum = float(np.sum(matrix))
total_avr = float(np.mean(matrix))

sum_main_diag = float(np.trace(matrix))
avr_main_diag = float(np.trace(matrix) / matrix.shape[0])

sum_sec_diag = float(np.trace(np.fliplr(matrix)))
avr_sec_diag = float(np.trace(np.fliplr(matrix)) / matrix.shape[0])

max_value = float(np.max(matrix))
min_value = float(np.min(matrix))

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
with open('../result/output_data_1.json', 'w') as json_file:
    json.dump(result, json_file)

normalized_matrix = (matrix - np.min(matrix)) / (np.max(matrix) - np.min(matrix))

np.save('../result/normalized_matrix_1.npy', normalized_matrix)