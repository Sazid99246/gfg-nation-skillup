class Solution:
    def equalizeArray(self, N, k, A):
        MOD = 10**9 + 7
        
        # Step 1: check possibility
        rem = A[0] % k
        for a in A:
            if a % k != rem:
                return -1
        
        # Step 2: sort and find median
        A.sort()
        median = A[N // 2]
        
        # Step 3: calculate moves
        moves = 0
        for a in A:
            moves += abs(a - median) // k
        
        return moves % MOD
