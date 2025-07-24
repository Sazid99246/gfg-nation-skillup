def isPalindrome(s):
    s = s.lower()
    reversed_s = s[::-1]
    return s == reversed_s