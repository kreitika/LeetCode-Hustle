class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [(capital[i], profits[i]) for i in range(len(capital))]
        projects.sort()
        idx = 0
        max_profit_heap = []

        for _ in range(k):
            while idx < len(projects) and projects[idx][0] <= w:
                heapq.heappush(max_profit_heap, -projects[idx][1])
                idx += 1

            if not max_profit_heap: break
            w+= -heapq.heappop(max_profit_heap)

        return w

        