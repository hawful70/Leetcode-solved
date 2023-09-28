from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        odd = head
        even = head.next
        ehead = even

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = ehead
        return head

    
solution = Solution()

head = ListNode(1)
second_node = ListNode(2)
third_node = ListNode(3)
four_node = ListNode(4)
five_node = ListNode(5)

head.next = second_node
second_node.next = third_node
third_node.next = four_node
four_node.next = five_node


solution.oddEvenList(head)