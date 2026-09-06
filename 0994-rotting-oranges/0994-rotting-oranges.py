class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2 : 
                    queue.append((r, c , 0))
                elif grid[r][c] == 1:
                    fresh += 1

        max_time = 0

        while queue:
            r,c, time = queue.popleft()
            max_time = max(max_time, time)

            for dr, dc in [(-1,0), (1,0), (0, -1), (0, 1)]:
                new_r, new_c = r + dr, c + dc
                if (0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1):
                    grid[new_r][new_c] = 2

                    fresh -= 1

                    queue.append((new_r, new_c, time + 1))


        return max_time if fresh == 0 else -1 


        