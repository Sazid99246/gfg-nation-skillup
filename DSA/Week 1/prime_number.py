import math


class Solution:
    def isPrime(self, n):
        if n < 2:
            return False
        else:
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
                    break
        return True


s = Solution()
print(s.isPrime(7))
print(s.isPrime(25))
print(s.isPrime(1))
