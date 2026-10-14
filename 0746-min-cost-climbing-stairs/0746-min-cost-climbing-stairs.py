class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        a, b = 0, 0 
        n = len(cost)

        for i in range(2, n +1):
            a, b = b, min(b + cost[i - 1], a + cost[i - 2])

        return b 
        