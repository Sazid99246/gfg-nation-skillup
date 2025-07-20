class Solution:
    def isPrime(self, n):
        if n < 2:
            return False
        else:
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
                    break
        return True

    def primeFac(self, n):
        result = []
        for i in range(2, n + 1):
            if n % i == 0 and self.isPrime(i):
                result.append(i)
        return result
