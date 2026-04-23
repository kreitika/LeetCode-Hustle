class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        maxM = 0

        for L in range(len(s)):
            mySet = set()
            count = 0
            for R in range(L, len(s)):
                if s[R] not in mySet :
                    mySet.add(s[R])
                    count += 1
                    if R == len(s) - 1 : maxM = max(count, maxM)
                else:
                    maxM = max(count, maxM)
                    break
                
        return maxM