class Solution:
    def vowelCount(self, s):    
        v = "aeiou"
        f = {}

        # Count frequency of each vowel in the string
        for c in s:
            if c in v:
                f[c] = f.get(c, 0) + 1

        freq = []

        # Build frequency list of distinct vowels in order
        for ch in v:
            if ch in f:
                freq.append(f[ch])

        k = len(freq)
        if k == 0:
            return 0  # No vowels found

        dp = [-1] * (1 << k)

        # Recursive helper function
        def count(mask):
            if mask == (1 << k) - 1:
                return 1  # All vowels used

            if dp[mask] != -1:
                return dp[mask]

            total = 0
            for i in range(k):
                if (mask & (1 << i)) == 0:
                    total += freq[i] * count(mask | (1 << i))

            dp[mask] = total
            return total

        return count(0)

# Test
s = Solution()
print(s.vowelCount("aaxyze"))
