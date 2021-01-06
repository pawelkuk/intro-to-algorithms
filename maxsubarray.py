def maximum_cross_subarray(arr: list[int]):
    mid = len(arr) // 2
    left_idx = mid
    tmp_sum = 0
    curr_left_max_sum = 0
    for idx, el in zip(range(mid - 1, -1, -1), arr[:mid][::-1]):
        tmp_sum += el
        if tmp_sum > curr_left_max_sum:
            curr_left_max_sum = tmp_sum
            left_idx = idx

    tmp_sum = 0
    curr_right_max_sum = 0
    right_idx = mid
    for idx, el in zip(range(mid, len(arr)), arr[mid:]):
        tmp_sum += el
        if tmp_sum > curr_right_max_sum:
            curr_right_max_sum = tmp_sum
            right_idx = idx
    return arr[left_idx : right_idx + 1]


def maximum_subarray(arr: list[int]) -> list[int]:
    # print(arr)
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    case_1 = maximum_subarray(arr[:mid])
    case_2 = maximum_cross_subarray(arr)
    case_3 = maximum_subarray(arr[mid:])
    return max(case_1, case_2, case_3, key=lambda x: sum(x))


assert maximum_subarray([1, 2, 3, 4]) == [1, 2, 3, 4]
assert maximum_subarray([]) == []
assert maximum_subarray([1]) == [1]
assert maximum_subarray([1, -1]) == [1]
assert maximum_subarray([1, 2, 3, 4, -100, 4, 5, 6]) == [4, 5, 6]
assert maximum_subarray([2, -1, 3, -2, 5, -100, 1, 2, 1, 1]) == [2, -1, 3, -2, 5]
