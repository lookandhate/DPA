from utils import my_sum, my_len, my_max


def algorithm_using_standart_library(nums: list[int]) -> list[int]:
    if not nums:
        return []


    average = sum(nums) / len(nums)
    max_element_index = nums.index(max(nums))
    return list(filter(lambda x: x >= average or nums.index(x) < max_element_index, nums))


def algorithm_without_standart_library(nums: list[int]) -> list[int]:
    if not nums:
        return []

    average = my_sum(nums) / my_len(nums)
    max_element_index = nums.index(my_max(nums))
    return [x for x in nums if x >= average or nums.index(x) < max_element_index]
