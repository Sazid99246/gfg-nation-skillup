import math


class Solution:
    def divFloorCeil(self, a, b):
        return [math.floor(a / b), math.ceil(a / b)]


s = Solution()
print(s.divFloorCeil(5, 3))
