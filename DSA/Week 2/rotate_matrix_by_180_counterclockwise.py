class Solution:
    def rotateMatrix(self, matrix):
        n = len(matrix)

        # Step 1: Reverse each row (left to right)
        for i in range(n):
            matrix[i].reverse()

        # Step 2: Reverse columns (top to bottom)
        for j in range(n):
            top, bottom = 0, n - 1
            while top < bottom:
                matrix[top][j], matrix[bottom][j] = matrix[bottom][j], matrix[top][j]
                top += 1
                bottom -= 1
