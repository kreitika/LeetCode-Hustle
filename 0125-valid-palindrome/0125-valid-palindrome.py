class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(ch for ch in s if ch.isalnum())
        cleaned = cleaned.lower()

        front, back = 0,len(cleaned) - 1 
        def isPalRec(cleaned,left, right):
            if left < right:
                if cleaned[left] != cleaned[right]: return False
                left += 1
                right -= 1
                return isPalRec(cleaned, left, right)
            else: return True
        return isPalRec(cleaned, front, back)
        
        