# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l, r = 1, length - 2 # since first and last vals wont be peak obviously

        while l <= r:
            m = (l + r)//2
            left, mid, right = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)
            # left portion
            if left < mid < right :
                l = m + 1
            #right portion
            elif left > mid > right:
                r = m - 1
            # found peak
            else:
                break
        peak = m 

        # search left portion for target
        l,r = 0, peak
        while l <= r:
            m = (l + r)//2
            mid = mountainArr.get(m)
            if target < mid:
                r = m - 1
            elif target > mid:
                l = m + 1
            else: return m
        #search right portion for target
        l, r = peak, length - 1
        while l <= r:
            m = (l + r)//2
            mid = mountainArr.get(m)
            if target > mid:
                r = m - 1
            elif target < mid:
                l = m + 1
            else: return m
        return -1

        