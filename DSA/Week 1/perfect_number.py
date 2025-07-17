import math

class Solution:
    def isPerfect(self, n):
        if n < 2:
            return False

        total = 1

        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                total += i
                if i != n // i:
                    total += n // i

        return total == n

s = Solution()
print(s.isPerfect(6))
print(s.isPerfect(10))
