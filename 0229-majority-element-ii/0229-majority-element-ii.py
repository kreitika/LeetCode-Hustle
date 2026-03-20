class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = nums[0]
        cand2 = 0
        for i in range(len(nums)):
            if nums[i] != cand1 :
                 cand2 = nums[i]
                 break

        count1, count2 = 0, 0
        for i in range( len(nums)):
            if nums[i] == cand1 : count1+=1
            elif nums[i] == cand2 : count2+=1
            
            elif count1 == 0 : 
                cand1 = nums[i]
                count1 = 1
            elif count2 == 0 : 
                cand2 = nums[i]
                count2 = 1
            else : 
                count1-=1
                count2-=1
        print(cand1, cand2)
        temp1, temp2 = 0, 0
        for i in range(len(nums)):
            if nums[i] == cand1 : temp1+=1
            if nums[i] == cand2 and cand2 != cand1 : temp2+=1
        ans = []
        if temp1 > len(nums)//3 : ans.append(cand1)
        if temp2 > len(nums)//3 : ans.append(cand2)

        return ans