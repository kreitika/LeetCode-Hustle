class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        unique_vals = sorted(count.keys())
        result = []

        def backtrack(index, current):
            if index == len(unique_vals):
                result.append(current.copy())
                return
            value = unique_vals[index]
            max_count = count[value]
            for i in range(max_count + 1):
                current.extend([value]* i)
                backtrack(index + 1,current )
                
                for _ in range(i):
                    current.pop()

            

        backtrack(0, [])
        return result
        