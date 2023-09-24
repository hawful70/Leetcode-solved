from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currentListNode = mergedListNode = ListNode()
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                currentListNode.next = list1
                list1 = list1.next
            else:
                currentListNode.next = list2
                list2 = list2.next
            currentListNode = currentListNode.next

        if list1 != None:
            currentListNode.next = list1
        if list2 != None:
            currentListNode.next = list2

        return mergedListNode.next
    
head = ListNode(1)
second_node = ListNode(2)
third_node = ListNode(4)

head.next = second_node
second_node.next = third_node

head2 = ListNode(1)
second_node2 = ListNode(3)
third_node2 = ListNode(4)

head2.next = second_node2
second_node2.next = third_node2

solution = Solution()
print(solution.mergeTwoLists(head, head2))
