class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else: 
                return m
        if target > nums[m]:
            for i in range(m, r + 1):
                if nums[i] > target: 
                    return i
            return r + 1
        if target <  nums[m]:
            for i in range(l, m):
                if nums[i] < target: 
                    return i
            return l
        
            

        