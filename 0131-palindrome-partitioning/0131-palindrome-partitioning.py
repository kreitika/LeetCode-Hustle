class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s)

        def isPalin(sub):
            return sub == sub[:: -1]

        def backtrack(start, current):
            if start == n:
                result.append(current.copy())
                return

            for end in range(start + 1, n + 1):
                sub = s[start : end]
                if isPalin(sub):
                    current.append(sub)
                    backtrack(end, current)
                    current.pop()
        backtrack(0, [])
        return result
        