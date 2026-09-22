class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights : return []

        reachable_pac = set()
        reachable_atl = set()

        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, visited, prev_h):
            if r < 0 or r >= rows or c < 0 or c >= cols or \
            prev_h> heights[r][c] or (r,c) in visited: return

            visited.add((r, c))

            for dr,dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(r + dr, c + dc, visited, heights[r][c])

        
        for c in range(cols):
            dfs(0, c, reachable_pac, heights[0][c] )
            dfs(rows - 1, c, reachable_atl, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, reachable_pac, heights[r][0])
            dfs(r, cols - 1, reachable_atl, heights[r][cols - 1] )

        result = []

        for r in range(rows):
            for c in range(cols):
                if (r,c) in reachable_pac and (r,c) in reachable_atl :
                    result.append((r,c))

        return result 



        




        