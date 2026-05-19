class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r
        while l <= r:
            m = (l + r)//2
            hours = 0
            for i in piles:
                hours += math.ceil(i/m)
            if hours > h :
                l = m + 1
            elif hours <= h :
                r = m - 1
                res = min(res,m)
        return res
            


        