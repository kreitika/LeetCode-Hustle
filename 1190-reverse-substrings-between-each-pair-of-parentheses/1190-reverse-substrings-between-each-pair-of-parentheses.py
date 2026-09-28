class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair, stack = {}, []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                j = stack.pop()
                pair[i], pair[j] = j, i

        res = []
        i, d = 0, 1
        while 0 <= i < n:
            if s[i] in '()':
                i = pair[i]
                d = -d
            else:
                res.append(s[i])
            i += d
        return ''.join(res)   
        