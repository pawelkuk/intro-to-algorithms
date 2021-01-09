from functools import lru_cache
from itertools import chain
from statistics import median
import math
from typing import Tuple, List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()

        @lru_cache(None)
        def solve(idx, n, k):
            if k == 1:
                mid = houses[(n + idx) // 2]
                return sum([abs(houses[i] - mid) for i in range(idx, n + 1)])
            result = float("inf")
            for i in range(idx, n + 1):
                if n - i < k - 1:
                    break
                result = min(result, solve(idx, i, 1) + solve(i + 1, n, k - 1))
            return result

        return solve(0, len(houses) - 1, k)


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
