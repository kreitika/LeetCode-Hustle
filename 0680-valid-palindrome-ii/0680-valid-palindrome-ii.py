class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPal(left, right, s):
            while left < right:
                if s[left] != s[right]: return False
                left += 1
                right -= 1
            return True
        
        left, right = 0,len(s) - 1
        while left < right :
            if s[left] != s[right]:
                return isPal(left + 1, right, s) or isPal(left, right - 1, s)
            left += 1
            right -= 1
            
        return True