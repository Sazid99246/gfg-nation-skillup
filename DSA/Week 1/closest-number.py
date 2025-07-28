class Solution:
    def closestNumber(self, n, m):
        q = n // m
        
        low = q * m
        hig = (q + 1) * m 
        
        if abs(low - n) < abs(hig - n):
            return low
        elif abs(low - n) > abs(hig - n):
            return hig
        else:
            return max(low, hig, key=abs)

s = Solution()
print(s.closestNumber(12, 4))
print(s.closestNumber(-18, 6))