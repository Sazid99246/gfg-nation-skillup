import math

class Solution:
    def countNumbers(self, n):
        def sieve(limit):
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(math.sqrt(limit)) + 1):
                if is_prime[i]:
                    for j in range(i*i, limit + 1, i):
                        is_prime[j] = False
            return [i for i, val in enumerate(is_prime) if val]

        count = 0
        limit = int(n ** 0.25) + 1
        primes = sieve(int(n ** 0.5) + 1)

        # Case 1: p^8
        for p in primes:
            if p ** 8 <= n:
                count += 1
            else:
                break

        # Case 2: p^2 * q^2
        num_primes = len(primes)
        for i in range(num_primes):
            for j in range(i + 1, num_primes):
                val = (primes[i] ** 2) * (primes[j] ** 2)
                if val <= n:
                    count += 1
                else:
                    break

        return count

# Example usage
s = Solution()
print(s.countNumbers(100))  # Output: 2
print(s.countNumbers(200))  # Output: 3
