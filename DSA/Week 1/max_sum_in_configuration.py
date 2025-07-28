class Solution:
    def maxSum(self, a):
        # code here
        sm = 0
        ism = 0
        n = len(a)
        for i in range(n):
            sm += a[i]
            ism += i*a[i]
        ans = ism
        for i in range(n):
            ism = ism+sm-n*a[n-1-i]
            if ism > ans:
                ans = ism
        return ans
