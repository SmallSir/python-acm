#Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return
        p = head
        l = ListNode(0)
        l.next = p
        while head.next:
            if head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
        return l.next