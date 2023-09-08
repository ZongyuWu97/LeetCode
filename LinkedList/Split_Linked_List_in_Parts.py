# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        tmp = head
        count = 0
        while tmp:
            count += 1
            tmp = tmp.next
        
        ans = []
        while k:
            ans.append(head)
            prev = ListNode(0, head)
            curr = count
            for _ in range((curr + k - 1) // k):
                count -= 1
                head = head.next
                prev = prev.next
            prev.next = None
            k -= 1
        return ans
