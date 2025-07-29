class Solution:
    def balanceSums(self, mat):
        n = len(mat)
        res = 0
        maxSum = 0
        
        # Find maximum sum across all rows
        for i in range(n):
            sum = 0
            for j in range(n):
                sum += mat[i][j]
            maxSum = max(sum, maxSum)
        
        # Find maximum sum across all columns
        for j in range(n):
            sum = 0
            for i in range(n):
                sum += mat[i][j]
            maxSum = max(sum, maxSum)
        
        # Sum of operations across all rows
        for i in range(n):
            sum = 0
            for j in range(n):
                sum += mat[i][j]
            res += (maxSum - sum)
        
        return res
