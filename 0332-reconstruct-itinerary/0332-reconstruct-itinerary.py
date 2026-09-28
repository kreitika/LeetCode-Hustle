class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = defaultdict(list)

        for src, dst in tickets :
            heapq.heappush(graph[src], dst)

        route = []

        def dfs(airport):
            while graph[airport]:
                next_airp = heapq.heappop(graph[airport])

                dfs(next_airp)
            route.append(airport)

        dfs("JFK")

        return route[::-1] 
        