from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current_l1, current_l2 = l1, l2
        node, remainder, z = ListNode(), 0, 0
        head = node
        while current_l1 or current_l2:
            z = (current_l1.val if current_l1 else 0) + (current_l2.val if current_l2 else 0) + remainder
            remainder, node.val = divmod(z, 10)
            if current_l1:
                current_l1 = current_l1.next
            if current_l2:
                current_l2 = current_l2.next
            if current_l1 or current_l2:
                node.next = ListNode()
                node = node.next
        node.next = ListNode(remainder) if remainder else None
        return head
