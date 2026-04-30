class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        L = 0
        R = len(arr) - k
        while L < R :
            mid = (L + R)//2
            if x - arr[mid] > arr[mid + k] - x:
                L = mid + 1
            else :
                R = mid
        return arr[L: L + k] 