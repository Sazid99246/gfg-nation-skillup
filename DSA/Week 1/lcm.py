class Solution:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def lcm(self, a, b):
        return abs(a * b) // self.gcd(a, b)


s = Solution()
print(s.lcm(12, 18))
