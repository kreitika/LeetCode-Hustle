class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 : return 0
        mySet = set()
        for i in nums:
            mySet.add(i)
        
        start_num = []

        for i in mySet:
            if (i-1) not in mySet : start_num.append(i)
        
        max_seq = 1

        for i in start_num:
            count = 1
            while(i+1 in mySet):
                count+=1
                i+=1
            if count > max_seq : max_seq = count

        return max_seq