"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r, c, size):
            all_same = True
            for i in range(size):
                for j in range(size):
                    if grid[r][c] != grid[r + i][c + j]:
                        all_same = False
                        break
            if all_same:
                return Node(
                    grid[r][c] == 1,
                    True,
                    None,
                    None,
                    None,
                    None
                )
            half = size//2
            return Node(
                True,
                False,
                dfs(r,c, half),
                dfs(r,c+half,half),
                dfs(r + half, c, half),
                dfs(r + half, c + half, half)
            ) 
        return dfs(0, 0, len(grid))