class Solution:
    def modmul(self, a, b, M):
        return (a * b) % M


s = Solution()
print(s.modmul(5, 3, 11))
