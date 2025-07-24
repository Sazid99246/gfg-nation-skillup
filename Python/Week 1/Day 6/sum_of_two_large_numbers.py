class Solution:
    def findSum(self, s1, s2):
        
        # If one string is empty, return the other
        if not s1:
            return s2
        if not s2:
            return s1
        
        # Result string to store the sum
        result = []
        
        # Indices to traverse strings from end
        i = len(s1) - 1
        j = len(s2) - 1
        
        # Carry to handle digit sum > 9
        carry = 0
    
        # Traverse both strings from end
        while i >= 0 or j >= 0 or carry > 0:
            
            # Get current digits (0 if string exhausted)
            digit1 = int(s1[i]) if i >= 0 else 0
            digit2 = int(s2[j]) if j >= 0 else 0
            
            # Sum current digits and carry
            digitSum = digit1 + digit2 + carry
            
            # Update carry and current digit
            carry = digitSum // 10
            digitSum %= 10
            
            # Append current digit to result 
            result.append(str(digitSum))
            
            # Move indices
            i -= 1
            j -= 1
        
        # Remove leading zeros
        while len(result) > 1 and result[-1] == '0':
            result.pop()
        
        # Reverse the string 
        return ''.join(result[::-1])

s = Solution()
print(s.findSum("25", "23"))