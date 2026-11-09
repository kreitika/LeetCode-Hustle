class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        cur_max = cur_min = best = nums[0]

        for i in range(1, len(nums)):
            cands = (nums[i], cur_max*nums[i], cur_min*nums[i])
            cur_max = max(cands)
            cur_min = min(cands)
            best = max(best, cur_max)

        return best
        