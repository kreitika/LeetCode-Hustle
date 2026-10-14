class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1 : return nums[0]

        def robline(lo, hi):
            m = hi - lo + 1
            a, b = 0, 0

            for i in range(lo, hi + 1):
                a, b = b , max(b , a + nums[i])

            return b 
        


        return max(robline(0, n - 2), robline(1, n - 1))