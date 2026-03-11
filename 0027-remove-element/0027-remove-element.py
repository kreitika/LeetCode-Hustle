class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr1,ptr2=0,0
        count=0
        while ptr1< len(nums):
            if (nums[ptr1]!=val)and (nums[ptr2]!=val):
                ptr2+=1
                
            elif nums[ptr1]==val:
                count+=1
            elif (nums[ptr1] !=val) and (nums[ptr2]==val):
                nums[ptr2]=nums[ptr1]
                nums[ptr1]=val
                ptr2+=1
            ptr1+=1
        print(nums)
        return len(nums)-count