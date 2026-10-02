class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        visited = set()
        min_heap = [(grid[0][0], 0, 0)]
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while min_heap:
            elevation, row, col = heapq.heappop(min_heap)

            if (row, col) in visited : continue

            visited.add((row,col))
            if row == n - 1 and col == n - 1:
                return elevation

            for dr, dc in directions:
                nr, nc = row + dr, col + dc 
                if 0 <= nr and nr <= n - 1 and 0 <= nc and nc <= n - 1 and (nr,nc) not in visited :
                    new_elevation = max(elevation, grid[nr][nc])
                    heapq.heappush(min_heap, (new_elevation, nr, nc))

        return -1 
        