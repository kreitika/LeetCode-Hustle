# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([root])
        result = []
        while q:
            level = []
            for _ in range(len(q)):
                temp = q.popleft()
                level.append(temp.val)
                if temp.left: q.append(temp.left)
                if temp.right: q.append(temp.right)
            result.append(level)
        return result


        