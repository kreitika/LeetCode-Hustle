class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = list(range(n + 1))

        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]

            return node


        def union(a, b):
            root_a, root_b = find(a), find(b)
            if root_a == root_b: return False

            parent[root_a] = root_b
            return True



        for a,b in edges:
            if not union(a,b): return [a,b]

        return []

    
        