# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0,head)
        current = dummy
        while current.next and current.next.next:
            left = current.next
            right = left.next

            current.next = right
            left.next = right.next
            right.next = left
            current = left
        return dummy.next