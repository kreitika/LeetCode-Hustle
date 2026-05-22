class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total//2
        if len(A) > len(B):
            A,B = B,A #A is the shorter one

        l, r = 0, len(A) - 1
        while True :
            m = (l + r)//2 # index of A
            j = half - m - 2 #index of B

            Aleft = A[m] if m >= 0 else float("-infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Aright = A[m + 1] if m + 1< len(A) else float("infinity")
            Bright = B[j + 1] if j + 1< len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright :
                if total%2 != 0:
                     #odd
                     return min(Aright,Bright)
                return (max(Aleft,Bleft) + min(Aright, Bright))/2
            elif Aleft > Bright :
                #A ko small karo
                r = m - 1
            else:
                #Bleft > Aright : A ko big karo
                l = m + 1


            
        