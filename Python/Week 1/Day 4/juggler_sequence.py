class Solution:
    def jugglerSequence(self, n):
        result = [1]
        while n != 1:
            if n % 2 == 0:
                n = int(n ** 0.5)
                result.append(n)
            else:
                n = int(n ** 1.5)
                result.append(n)
        return result

s = Solution()
print(s.jugglerSequence(9))
            