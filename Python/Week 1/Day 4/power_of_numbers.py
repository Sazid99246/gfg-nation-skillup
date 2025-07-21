class Solution:
    def reverseexponentiation(self, n):
        if n < 10:
            return n ** n
        else:
            return 10
