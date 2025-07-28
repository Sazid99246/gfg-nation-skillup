class Solution:
    def swapDiagonal(self, mat):
        size = len(mat)
        
        for i in range(size):
    
            # Swap major and minor diagonal elements
            mat[i][i], mat[i][size - i - 1] = mat[i][size - i - 1], mat[i][i]
