class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        idx = 0
        def backtrack(idx, current):
            if idx == len(nums):
                result.append(current.copy())
                return
            backtrack(idx + 1, current)

            current.append(nums[idx])
            backtrack(idx + 1, current)
            current.pop()
        
        backtrack(0, [])

        return result 
        