class Solution:
    def countPrimes(self, n: int) -> int:
        sieve = [False] * n
        res = 0

        for i in range(2, n):
            if not sieve[i]:
                res += 1
                for j in range(i * i, n, i):
                    sieve[j] = True

        return res