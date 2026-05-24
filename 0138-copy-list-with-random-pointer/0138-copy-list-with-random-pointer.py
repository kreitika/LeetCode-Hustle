"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldNodeCopy = {None : None}
        curr = head
        while curr:
            copy = Node(curr.val)
            oldNodeCopy[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = oldNodeCopy[curr]
            copy.next = oldNodeCopy[curr.next]
            copy.random = oldNodeCopy[curr.random]
            curr = curr.next
        return oldNodeCopy[head]

        