# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = midpoint = head
        while fast and fast.next:
            midpoint = midpoint.next
            fast = fast.next.next
        list2 = self._reverse_list(midpoint.next)
        midpoint.next = None
        while list2:
            tmp1, tmp2 = head.next, list2.next
            head.next = list2
            head = tmp1
            list2.next = head
            list2 = tmp2

    def _reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        prev = None
        while ptr:
            nxt = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = nxt
        return prev