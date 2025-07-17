class Solution:
    def gcd(self, a, b):
        bigger = max(a, b)
        smaller = min(a, b)

        while bigger % smaller != 0:
            remainder = bigger % smaller
            bigger = smaller
            smaller = remainder

        return smaller


s = Solution()
print(s.gcd(20, 28))
