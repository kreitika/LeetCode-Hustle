class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=1
        nums.sort()
        return nums[len(nums)//2]

