class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = {i : [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {i : float('inf') for i in range(1, n + 1)}
        dist[k] = 0

        heap = [(0, k)]

        while heap :
            curr_dist, node = heapq.heappop(heap)

            if curr_dist > dist[node]:
                continue

            for neigh, weight in graph[node]:
                new_dist = curr_dist + weight
                if new_dist < dist[neigh]:
                    dist[neigh] = new_dist
                    heapq.heappush(heap, (new_dist, neigh))

        max_dist = max(dist.values())

        return max_dist if max_dist < float('inf') else -1
        