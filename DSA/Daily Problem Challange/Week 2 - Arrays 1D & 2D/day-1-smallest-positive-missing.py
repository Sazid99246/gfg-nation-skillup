class Solution:
    def missingNumber(self, arr):
        arr = [x for x in arr if x > 0]
        arr.sort()
        
        smallest = 1

        for num in arr:
            if num == smallest:
                smallest += 1

        return smallest
