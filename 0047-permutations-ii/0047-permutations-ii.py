class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        used = [False]*len(nums)

        def backtrack(current):
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for i in range(len(nums)):
                if used[i]: continue

                if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False:
                    continue
            
                current.append(nums[i])
                used[i] = True
                backtrack(current)

                current.pop()
                used[i] = False

        backtrack([])

        return result

        