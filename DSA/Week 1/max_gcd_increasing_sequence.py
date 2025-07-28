class Solution:
    def maxGcdSeq(self, n, m):
        # Try possible gcd values from high to low
        for g in range(n // (m * (m + 1) // 2), 0, -1):
            seq = [g * i for i in range(1, m)]
            last = n - sum(seq)
            if last > seq[-1] and last % g == 0:
                seq.append(last)
                return seq
        return [-1]
