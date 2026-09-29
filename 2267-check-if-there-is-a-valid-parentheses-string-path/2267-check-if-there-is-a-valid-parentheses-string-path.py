class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == ')' : return False
        if grid[m - 1][n - 1] == '(': return False
        visited = set()

        def dfs(i, j, bal):
            if i > m - 1 or j > n - 1 : return False
            nb = bal + (1 if grid[i][j] == '(' else -1 )
            if nb < 0 : return False
            if nb > m - 1 - i + n - 1 - j : return False
            if i == m - 1 and j == n - 1: return nb == 0
            state = (i, j, nb)
            if state in visited : return False
            visited.add(state)

            return dfs(i + 1, j, nb) or dfs(i, j + 1, nb)

        return dfs(0, 0, 0)

        