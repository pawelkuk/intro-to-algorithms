def binary_search(arr: list, target: int):
    min_ = 0
    max_ = len(arr) - 1
    while True:
        if max_ < min_:
            return -1
        avg = int((min_ + max_) / 2)
        if arr[avg] == target:
            return avg
        elif arr[avg] < target:
            min_ = avg + 1
        elif arr[avg] > target:
            max_ = avg - 1
        else:
            raise ValueError("Illegal state")


assert binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == 10
assert binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9) == 9
assert binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8) == 8
assert binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7) == 7
assert binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6) == 6
assert binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 5
assert binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0) == 0
