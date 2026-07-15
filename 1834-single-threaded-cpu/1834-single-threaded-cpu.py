class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed = sorted(enumerate(tasks), key = lambda x : x[1][0])
        heap = []
        result = []
        time = 0
        i = 0
        while len(result) < len(tasks):
            while i < len(indexed) and indexed[i][1][0] <= time:
                idx , task = indexed[i]
                heapq.heappush(heap, (task[1], idx))
                i += 1
            if heap:
                proc_time, idx = heapq.heappop(heap)
                time += proc_time
                result.append(idx)
            else:
                time = indexed[i][1][0]
        return result
