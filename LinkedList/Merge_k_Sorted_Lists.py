# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        if n == 2:
            return self.merge(lists[0], lists[1])
        return self.merge(self.mergeKLists(lists[:n // 2]), self.mergeKLists(lists[n // 2:]))
    
    def merge(self, l1, l2):
        dummy = head = ListNode()
        while l1 and l2:
            tmp = l1.val if l1.val < l2.val else l2.val
            if l1.val < l2.val:
                l1 = l1.next
            else:
                l2 = l2.next
            head.next = ListNode(tmp)
            head = head.next
        head.next = l1 if l1 else l2
        return dummy.next
            
            
