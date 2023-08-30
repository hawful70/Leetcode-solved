from functools import lru_cache

class Solution(object):
    @lru_cache(None)
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)