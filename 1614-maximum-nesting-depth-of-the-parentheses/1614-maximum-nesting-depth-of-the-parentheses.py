class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxCount = 0
        for i in range(len(s)):
            if s[i] != '(' and s[i] != ')': 
                continue
            if s[i] == '(' : 
                count += 1
            elif s[i] == ')':
                maxCount = max(count, maxCount)
                count -= 1

        return maxCount 

        