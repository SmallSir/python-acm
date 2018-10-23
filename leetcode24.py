class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        start = ListNode(0)
        p = start
        q = start.next
        while q!=None and q.next!=None:
            p.next = q.next
            q.next = p.next.next
            p.next.next = q
            p = q
            q = q.next
        return start.next

