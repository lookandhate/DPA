from algorithms import algorithm_without_standart_library, algorithm_using_standart_library


def test_default():
    nums = [8, 6, 9, 4, 5]
    assert algorithm_using_standart_library(nums) == [8, 6, 9] == algorithm_without_standart_library(nums)


def test_no_input():
    nums = []
    assert algorithm_using_standart_library(nums) == [] == algorithm_without_standart_library(nums)


def test_no_unique():
    nums = [1, 1, 1, 1, 1]
    assert algorithm_using_standart_library(nums) == [1, 1, 1, 1, 1] == algorithm_without_standart_library(nums)


def test_one_unique():
    nums = [6, 5, 5, 5]
    assert algorithm_using_standart_library(nums) == [6] == algorithm_without_standart_library(nums)
