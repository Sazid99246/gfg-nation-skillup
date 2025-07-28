class Solution:
    def printDivisors(self, n):
        divisors = []

        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)

        return divisors

s = Solution()
print(s.printDivisors(10))
print(s.printDivisors(100))
print(s.printDivisors(100000))