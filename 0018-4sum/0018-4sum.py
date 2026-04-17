class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums, target, k, start):
            result = []
            if k == 2:
                l,r = start, len(nums) - 1
                while l < r:
                    summ = nums[l] + nums[r]
                    if summ < target:
                        l += 1
                    elif summ > target:
                        r -= 1
                    else:
                        ans = [nums[l], nums[r]]
                        result.append(ans)
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l+=1
                return result

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]: continue
                for subset in kSum(nums, target - nums[i],k - 1,i + 1):
                    result.append([nums[i]] + subset)
            return result
        
        nums.sort()
        return kSum(nums, target,4,0)
                    
       