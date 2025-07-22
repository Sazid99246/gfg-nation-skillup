class Solution:
    def reverseingroups(self, arr, k):
        n = len(arr)
        for i in range(0, n, k):
            start = i
            end = min(i + k - 1, n - 1)

            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
        return arr

            
        return reversed_arr

s=Solution()
print(s.reverseingroups([1, 2, 3, 4, 5], 3))