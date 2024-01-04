# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        
        s = []
        n = len(l)
        res = [0] * n
        for i, value in enumerate(l):
            while s and l[s[-1]] < value:
                smaller = s.pop()
                res[smaller] = value
            s.append(i)
        return res

        