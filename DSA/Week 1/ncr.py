class Solution:
    def nCr(self, n, r):
        if r > n:
            return 0
        return self.fact(n) // (self.fact(r) * self.fact(n - r))
            
    def fact(self, n):
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


s = Solution()
print(s.nCr(2, 0))