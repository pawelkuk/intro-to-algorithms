class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        mod = 10 ** 9 + 7
        for i in range(2 * n, 0, -1):
            if i % 2 == 0:
                res = (res * i / 2) % mod
            else:
                res = (res * i) % mod
        return res


s = Solution()
assert s.countOrders(1) == 1
assert s.countOrders(2) == 6
assert s.countOrders(3) == 90