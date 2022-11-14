# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = dummy = ListNode()
        quotient = 0
        tmp1, tmp2 = l1, l2
        while tmp1.next or tmp2.next:
            if not tmp1.next:
                tmp1.next = ListNode()
            if not tmp2.next:
                tmp2.next = ListNode()
            tmp1, tmp2 = tmp1.next, tmp2.next

        while l1:
            quotient, remainder = divmod(quotient + l1.val + l2.val, 10)
            head.next = ListNode(remainder)
            l1, l2, head = l1.next, l2.next, head.next
        if quotient:
            head.next = ListNode(quotient)
        return dummy.next
            
