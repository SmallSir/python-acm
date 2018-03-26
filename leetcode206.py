# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        l = None
        p = ListNode()
        while head:
            k = head.next
            head = head.next
            k.next = l
            l = l.next
        return l
