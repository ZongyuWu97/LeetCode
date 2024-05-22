# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        if count == n:
            return head.next

        prev = ListNode(0, head)
        curr = head
        while count > n:
            prev = prev.next
            curr = curr.next
            count -= 1
        prev.next = curr.next
        return head
