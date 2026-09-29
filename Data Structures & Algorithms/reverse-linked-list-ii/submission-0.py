# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        # Move prev to the node just before left
        for _ in range(left - 1):
            prev = prev.next

        # Start reversing
        curr = prev.next

        for _ in range(right - left):
            front = curr.next

            curr.next = front.next
            front.next = prev.next
            prev.next = front

        return dummy.next