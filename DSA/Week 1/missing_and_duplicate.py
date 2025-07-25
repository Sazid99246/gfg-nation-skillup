class Solution:
    def rotateclockwise(self, arr, k):
        n = len(arr)
        k = k % n

        def reverse(start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
