from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)

        return self.mergeTwoLists(left, right)



    def getMid(self, head: Optional[ListNode]):
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

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
    
solution = Solution()

head = ListNode(4)
second_node = ListNode(2)
third_node = ListNode(1)
four_node = ListNode(3)

head.next = second_node
second_node.next = third_node
third_node.next = four_node
print(solution.sortList(head))