class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max, min = 0, 0
        for n in nums:
            if n >= max : max = n
            if n <= min : min = n  
        arr = [0]*(max - min + 1)

        if min < 0 : offset = min
        else: offset = 0

        for n in nums:
            arr[n - offset]+=1
        
        print(arr)
        
        ans = []
        
        while k > 0:
            max_value, max_index = 0,0
            for i,n in enumerate(arr):
                if n >= max_value: 
                    max_value = n
                    max_index = i 
            arr[max_index] = 0
            ans.append(max_index + offset)
            k-=1
        
        return ans
                
