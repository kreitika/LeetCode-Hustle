class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        summ = 0
        length = float('inf')
        for R in range(len(nums)):
            summ += nums[R]
            while summ >= target :
                length = min(length, R - L + 1)
                summ -= nums[L]
                L += 1
        if length == float('inf') :return 0
        else: return length
            