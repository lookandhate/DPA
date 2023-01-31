from pprint import pprint

import numpy as np

from utils import generate_matrix

if __name__ == '__main__':
    m, n = map(int, input("Input m, n: ").split())

    matrix: np.ndarray = generate_matrix(m, n)
    max_value = matrix.max()
    altered_matrix = matrix / max_value
    pprint(altered_matrix)
