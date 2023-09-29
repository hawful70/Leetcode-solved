from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        left = head
        right = self.getMid(head)
        temp = right.next
        right.next = None
        right = temp

        reverseRight = None
        while right:
            nextNode = right.next
            right.next = reverseRight
            reverseRight = right
            right = nextNode

        maxTwin = 0
        while left != None and reverseRight != None:
            if left.val + reverseRight.val > maxTwin:
                maxTwin = left.val + reverseRight.val
            left = left.next
            reverseRight = reverseRight.next

        return maxTwin

    def getMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
    