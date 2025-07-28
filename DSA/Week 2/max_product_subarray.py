class Solution:
    def maxProduct(self,a):
        max1=a[0]
        min1=a[0]
        maxso=a[0]
        for i in range(1,len(a)):
            n=a[i]
            if n<0:
                max1,min1=min1,max1
            max1=max(n,n*max1)
            min1=min(n,n*min1)
            maxso=max(maxso,max1)
        return maxso