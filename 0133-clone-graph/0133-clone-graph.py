"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node : return None

        old_to_new = {}

        def dfs(original):
            if original in old_to_new: return old_to_new[original]

            copy = Node(original.val)

            old_to_new[original] = copy

            for nbr in original.neighbors:
                copy.neighbors.append(dfs(nbr))


            return copy

        return dfs(node)

        