class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul_p = 1
        mul_s = 1
        output = [1]*(len(nums))
        for i in range(len(nums)):
            output[i] *= mul_p
            mul_p *= nums[i]
        for i in range(len(nums)):
            output[len(nums)-1-i] *= mul_s
            mul_s *= nums[len(nums)-1-i]
        return output