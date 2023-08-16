# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        sml, lrg = [], []
        while head:
            if head.val < x:
                sml.append(head.val)
            else:
                lrg.append(head.val)
            head = head.next

        dummy = head = ListNode()
        for num in sml:
            head.next = ListNode(num)
            head = head.next
        for num in lrg:
            head.next = ListNode(num)
            head = head.next
        return dummy.next