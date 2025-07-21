class Solution:
    def subsetSums(self, arr):
        res = [0]
        for i in range(0,len(arr)):
            l = len(res)
            for j in range(l):
                res.append(arr[i]+res[j])
        return res