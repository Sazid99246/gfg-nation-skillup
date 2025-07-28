class Solution:
    def transpose(self, mat):
         return [list(row) for row in zip(*mat)]
