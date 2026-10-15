class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, max_len = 0, 0

        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] ==s[r]:
                l -= 1
                r += 1
            return (l + 1, r - l - 1)

        for i in range(len(s)):
            for l,r in ((i, i), (i, i + 1)):
                st, ln = expand(l,r)

                if ln > max_len:
                    start, max_len = st, ln

        return s[start: start + max_len]

        