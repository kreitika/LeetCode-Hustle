class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        
        #binary search to find row
        while top <= bottom :
            mid = (top + bottom)//2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else: break
        #in case target doesnt really exist in matrix and top keeps going down or bottom keeps going up
        if not (top <= bottom): return False

        # binary search to find target in row
        l,r = 0, cols - 1
        row = (top + bottom)//2
        while l <= r:
            mid = (l + r)//2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else: return True
        return False
        
        

        