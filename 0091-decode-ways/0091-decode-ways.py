class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        a = 1
        b = 1 if s[0] != '0' else 0

        for i in range(2, n + 1):
            cur = 0
            if s[i - 1] != '0':
                cur += b
            if 10 <= int(s[i-2: i]) <= 26 :
                cur += a
            
            a, b = b, cur
        return b