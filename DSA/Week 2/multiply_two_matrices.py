class Solution:
    def multiply(self, mat1, mat2):
        n = len(mat1)  # Since the matrices are n x n
        # Initialize result matrix with 0s
        result = [[0 for _ in range(n)] for _ in range(n)]

        # Matrix multiplication
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[i][j] += mat1[i][k] * mat2[k][j]

        return result
