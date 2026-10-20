class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def expand(l, r):
            ret = 0
            while l >= 0 and r < n and s[l] == s[r]:
                ret += 1
                l -= 1
                r += 1
            return ret

        
        total = 0
        for i in range(n):
            total += expand(i, i)
            total += expand(i, i + 1)

        return total


        