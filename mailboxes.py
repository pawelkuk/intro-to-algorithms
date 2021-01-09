from functools import lru_cache
from itertools import chain
from statistics import median
import math
from typing import Tuple, List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        self.houses = sorted(houses)
        return self.solve(0, len(houses), k)

    @lru_cache
    def solve(self, idx0, idx1, k: int) -> int:
        if idx1 - idx0 < k:
            print(f"return inf")
            return float("inf")
        if k == 1:
            # print(idx0, idx1)
            m = int(median(self.houses[idx0:idx1]))
            # print(f"{houses=}, {m=}")
            return sum(abs(x - m) for x in self.houses[idx0:idx1])
        case_1 = (
            self.solve(idx0, i, k - 1) + self.solve(i, idx1, 1)
            for i in range(idx0 + k - 1, idx1)
        )
        res = min(case_1)
        # print(res)
        return res


s = Solution()
houses = [1, 4, 8, 10, 20]
k = 3
assert s.minDistance(houses, k) == 5

s = Solution()
houses = [2, 3, 5, 12, 18]
k = 2
assert s.minDistance(houses, k) == 9

s = Solution()
houses = [7, 4, 6, 1]
k = 1
assert s.minDistance(houses, k) == 8

s = Solution()
houses = [3, 6, 14, 10]
k = 4
assert s.minDistance(houses, k) == 0

s = Solution()
assert s.minDistance([14, 4, 1, 6, 2], 3) == 3

assert (
    s.minDistance(
        [48, 23, 44, 42, 2, 7, 25, 18, 32, 20, 36, 31, 30, 26, 10, 33, 22], 10
    )
    == 10
)
