class Solution:
    def sumOfDigits(self, n):
        sum = 0

        while n > 0:
            sum += n % 10
            n = int(n / 10)

        return sum


s = Solution()
print(s.sumOfDigits(687))
print(s.sumOfDigits(12))
