# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val1, val2 = "", ""
        while l1:
            val1 = str(l1.val) + val1
            l1 = l1.next
        while l2:
            val2 = str(l2.val) + val2
            l2 = l2.next
        val = int(val1) + int(val2)

        answer = ListNode()
        dummy = answer

        while val > 0:
            dummy.val = val%10
            val = val//10
            if val > 0:
                temp = ListNode()
                dummy.next = temp
                dummy = dummy.next

        return answer


        