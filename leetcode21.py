# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if not l1  and not l2 :
            return None
        l = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                l.next = l2
                l2 = l2.next
            else:
                l.nex = l1
                l1 = l1.next
            l = l.next
        l.next = l1 or l2
        return l