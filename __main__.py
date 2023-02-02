from pprint import pprint

import numpy as np

from utils import generate_matrix, input_vals

if __name__ == '__main__':
    m, n = input_vals()

    matrix: np.ndarray = generate_matrix(m, n)
    max_value = matrix.max()
    altered_matrix = matrix / max_value
    pprint(altered_matrix)
