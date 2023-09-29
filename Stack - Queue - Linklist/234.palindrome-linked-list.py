from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
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

        while left != None and reverseRight != None:
            if left.val != reverseRight.val:
                return False
            left = left.next
            reverseRight = reverseRight.next
        return True
        
    def getMid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow