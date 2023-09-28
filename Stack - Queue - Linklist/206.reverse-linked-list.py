from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverseList = None

        while head:
            nodeNext = head.next
            head.next = reverseList
            reverseList = head
            head = nodeNext

        return reverseList
    
head = ListNode(1)
second_node = ListNode(2)
third_node = ListNode(3)
four_node = ListNode(4)
five_node = ListNode(5)

head.next = second_node
second_node.next = third_node
third_node.next = four_node
four_node.next = five_node

solution = Solution()
solution.reverseList(head)