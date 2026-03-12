class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(arr, l, r):
            pivot = arr[r]
            p = l
            for i in range(l, r):
                if arr[i] <= pivot:
                    arr[p], arr[i] = arr[i], arr[p]
                    p += 1
            arr[p], arr[r] = arr[r], arr[p]
            return p

        def quickSort(arr, l, r):
            if l >= r:
                return
            p = partition(arr, l, r)
            quickSort(arr, l, p-1)
            quickSort(arr, p+1, r)
            
        quickSort(nums, 0, len(nums)-1)
        return nums
    