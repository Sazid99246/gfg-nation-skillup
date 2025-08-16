class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        l, res, product = 0, 0, 1

        for r in range(n):
            product *= a[r]

            while product >= k and l <= r:
                product /= a[l]
                l += 1
            res += r - l + 1

        return res
