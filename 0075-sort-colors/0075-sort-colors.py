class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        max,min = 0, 0
        for el in nums:
            if el >= max: max = el
            if el <= min: min = el

        if min < 0: offset = min
        else: offset = 0

        arr = [0]*(max - min + 1)

        for n in nums:
            arr[n + offset]+=1
        print(arr)
        
        i,j = 0,0
        while i < len(arr):
            while arr[i] > 0:
                nums[j] = i + offset
                j+=1
                arr[i]-=1
            i+=1
