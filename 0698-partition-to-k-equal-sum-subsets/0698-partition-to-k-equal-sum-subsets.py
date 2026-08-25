class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0 : return False

        side_len = total//k

        nums.sort(reverse = True)

        if nums[0] > side_len : return False

        sides = [0]*k

        def backtrack(index):
            if index == len(nums): return True

            for i in range(k):
                if nums[index] + sides[i] <= side_len:
                    sides[i] += nums[index]

                    if backtrack(index + 1):
                        return True
                    sides[i] -= nums[index]
                
                if sides[i] == 0 : break

            return False

        return backtrack(0)
        