class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        visited = set()
        min_heap = [(0, 0)]
        
        total_cost = 0
        pts_covered  = 0

        while pts_covered < n :
            cost, pt = heapq.heappop(min_heap)

            if pt in visited: continue

            visited.add(pt)
            total_cost += cost
            pts_covered += 1

            for next_pt in range(n):
                if next_pt not in visited:
                    px, py = points[pt]
                    nx, ny = points[next_pt]
                    dist = abs(px - nx) + abs(py - ny)
                    heapq.heappush( min_heap, (dist, next_pt))

        return total_cost
        
        