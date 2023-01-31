from typing import Callable

from algorithms import algorithm_without_standart_library, algorithm_using_standart_library
from utils import generate_input, manual_input_list

if __name__ == '__main__':
    should_generate: bool = input('Generate input? (y/n): ').lower() == 'y'
    should_use_handwritten_algorithm: bool = input('Use handwritten algorithm? (y/n): ').lower() == 'y'

    nums: list[int] = generate_input() if should_generate else manual_input_list()

    if should_generate:
        print(f'Generated input: {" ".join(map(str, nums))}')

    algorithm: Callable = algorithm_without_standart_library \
        if should_use_handwritten_algorithm \
        else algorithm_using_standart_library

    result = algorithm(nums)

    print(f'Result is {" ".join(map(str, result))}')
