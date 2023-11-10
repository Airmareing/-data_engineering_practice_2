import numpy as np

matrix = np.load('../data/matrix_42_2.npy')
condition = matrix > 542

indices_i, indices_j = np.where(condition)
values_z = matrix[condition]

np.savez('../result/res_arr_2.npz', x=indices_i, y=indices_j, z=values_z)

size_before = matrix.nbytes
size_after = sum(arr.nbytes for arr in [indices_i, indices_j, values_z])

print(f"Размер исходной матрицы: {size_before} байт")
print(f"Размер полученных массивов: {size_after} байт")

np.savez_compressed('../result/res_arr_compressed_2.npz', x=indices_i, y=indices_j, z=values_z)

size_after_compressed = sum(arr.nbytes for arr in np.load('../result/res_arr_compressed_2.npz').values())

print(f"Размер полученных массивов (сжатый формат): {size_after_compressed} байт")