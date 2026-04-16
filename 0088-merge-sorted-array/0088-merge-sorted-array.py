class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pt1, pt2 = 0,0
        answer = []
        while (pt1 < m) and (pt2 < n):
            if nums1[pt1] <= nums2[pt2]:
                answer.append(nums1[pt1])
                pt1+=1
            else:
                answer.append(nums2[pt2])
                pt2+=1
        while pt1 < m:
            answer.append(nums1[pt1])
            pt1+=1
        while pt2 < n:
            answer.append(nums2[pt2])
            pt2+=1
        for i in range(len(answer)):
            nums1[i] = answer[i]

