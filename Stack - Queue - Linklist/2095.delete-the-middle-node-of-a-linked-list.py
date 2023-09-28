from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if head and not head.next:
            return None

        prev = ListNode(0, head)
        slow = fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next
        return head

        
    
    
head = ListNode(1)
second_node = ListNode(3)
third_node = ListNode(4)
four_node = ListNode(7)
five_node = ListNode(1)
six_node = ListNode(2)
seven_node = ListNode(6)

head.next = second_node
second_node.next = third_node
third_node.next = four_node
four_node.next = five_node
five_node.next = six_node
six_node.next = seven_node

solution = Solution()
solution.deleteMiddle(head)