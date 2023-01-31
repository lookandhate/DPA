def manual_input_list() -> list[int]:
    user_input = input('Enter a list of numbers separated by spaces: ')
    return list(map(int, user_input.split()))


def generate_input() -> list[int]:
    from random import randint

    values_to_generate = randint(2, 15)
    return [randint(0, 100) for _ in range(values_to_generate)]


def my_sum(nums: list[int]) -> int:
    s = 0
    for i in nums:
        s += i
    return s

def my_len(nums: list[int]) -> int:
    l = 0
    for i in nums:
        l += 1
    return l

def my_max(nums: list[int]) -> int:
    m = nums[0]
    for i in nums:
        if i > m:
            m = i
    return m