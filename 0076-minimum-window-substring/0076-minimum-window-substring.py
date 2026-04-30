class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        window = {}
        countT = {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1
        have = 0
        need = len(countT)
        res = [-1,-1]
        resLen = float("inf")
        L =0
        for R in range(len(s)):
            c = s[R]
            window[c] = window.get(c,0) + 1

            if  c in countT and window[c] == countT[c] : have += 1
            while have == need :
                if (R - L + 1) < resLen :
                    res = [L, R]
                    resLen = R - L + 1
                
                window[s[L]] -= 1
                if s[L] in countT and window[s[L]] < countT[s[L]]:
                    have -= 1
                L += 1
        L, R = res
        return s[L:R+1] if resLen != float("inf") else ""

        