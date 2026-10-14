class Solution:
    def rob(self, nums: list[int]) -> int:
        a, b = 0,0
        n = len(nums)

        for num in nums:
            a, b = b, max(b, a + num)

        return b 
        