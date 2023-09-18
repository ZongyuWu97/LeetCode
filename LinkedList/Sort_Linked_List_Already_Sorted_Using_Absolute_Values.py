# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pos = []
        neg = []
        while head:
            if head.val >= 0:
                pos.append(head.val)
            else:
                neg.append(head.val)
            head = head.next
        
        dummy = head = ListNode()
        while neg:
            head.next = ListNode(neg.pop())
            head = head.next
        for val in pos:
            head.next = ListNode(val)
            head = head.next
        return dummy.next