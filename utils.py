from typing import Iterable

import numpy as np


def generate_matrix(m: int, n: int) -> np.array:
    return np.random.rand(m, n)


def input_vals() -> Iterable[int]:
    try:
        vals = map(int, input("Input m, n: ").split())
        assert len(vals) == 2
        return vals
    except ValueError:
        print("Invalid input. Try again.")
        return input_vals()
    except AssertionError:
        print("Excepted 2 values. Try again.")
        return input_vals()
