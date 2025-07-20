class Solution:
    def countDivisible(self, arr, m):
        count = 0
        for i in range(1, m + 1):
            for n in range(len(arr)):
                if i % arr[n] == 0:
                    count += 1
                    break
        return count

s = Solution()
print(s.countDivisible([2, 3, 5], 10))