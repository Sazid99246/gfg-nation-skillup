class Solution:
    def sieve(self, n):
        prime = [True] * (n + 1)  # include index n
        prime[0] = prime[1] = False  # 0 and 1 are not prime

        p = 2
        while p * p <= n:
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1

        result = [p for p in range(2, n + 1) if prime[p]]
        return result

s = Solution()
print(s.sieve(50))
