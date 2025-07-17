class Solution:
    def findSum(self, n):
        return int((n * (n + 1)) / 2)


s = Solution()
print(s.findSum(3))
print(s.findSum(5))
