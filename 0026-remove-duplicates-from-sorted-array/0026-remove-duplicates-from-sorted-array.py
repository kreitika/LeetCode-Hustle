class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 200
        count = 0
        answer = []
        for i in range(len(nums)):
            if nums[i] != current:
                current = nums[i]
                count += 1
                answer.append( nums[i])
        
        for i in range(len(answer)):
            nums[i] = answer[i]
        return count
    

