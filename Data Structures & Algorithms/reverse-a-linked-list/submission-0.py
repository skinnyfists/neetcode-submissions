# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
        prev = None
        while pointer:
            print(pointer.val)
            nxt = pointer.next
            pointer.next = prev
            prev = pointer
            if not nxt:
                break
            pointer = nxt
        return pointer