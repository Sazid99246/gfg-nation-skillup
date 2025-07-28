class Solution:
    def decToBinary(self, n):
        binArr = []

        while n > 0:
            binArr.append(str(n % 2))
            n = n // 2

        binArr.reverse()

        return "".join(binArr)


s = Solution()
print(s.decToBinary(2))
print(s.decToBinary(10))
