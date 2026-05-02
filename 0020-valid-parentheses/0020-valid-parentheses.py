class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {
        ')': '(',
        ']': '[',
        '}': '{'
        }

        for c in s:

            if c in "([{":
                stack.append(c)

            else:
                if not stack or stack.pop() != mp[c]:
                    return False

        return len(stack) == 0

    