"""Поиск групп единиц в файле."""
import numpy as np
import os
import sys


def read_file(file: str) -> list:
    """Чтение из файла c обработкой негативных случаев."""
    try:
        matrix = np.loadtxt(file, dtype=int)
        if os.stat(file).st_size == 0:
            print("Файл пустой")
            sys.exit(0)
        return matrix.tolist()
    except IOError:
        print("Входной файл отсутствует.")
        sys.exit(0)


def find_crater(matrix: np.ndarray, i: int, j: int) -> bool:
    """Рекурсивный поиск кратера."""
    if i < 0 or i >= matrix.shape[0]:
        return False
    if j < 0 or j >= matrix.shape[1]:
        return False
    crater = matrix[i][j] == 1
    matrix[i][j] = 0
    if crater:
        find_crater(matrix, i, j + 1)
        find_crater(matrix, i, j - 1)
        find_crater(matrix, i + 1, j)
        find_crater(matrix, i - 1, j)
    return crater


def calculate(array: list) -> int:
    """Учёт найденных кратеров."""
    craters = 0
    matrix = np.asarray(array)
    for i in range(matrix.shape[1]):
        for j in range(matrix.shape[0]):
            if find_crater(matrix, i, j):
                craters += 1
    return craters


input_array = read_file("input_file.txt")
if not any(input_array):
    print("Здесь кратеров нет.")
else:
    result = calculate(input_array)
    print(f"Найдено кратеров: {result}")
