class Solution:
    def removeNthFromEnd(self, head, n):
        def digui(x):
            if x == None:
                return 1
            k = digui(x.next)
            if k == n + 1:
                if n == 1:
                    x.next = None
                else:
                    y = (x.next).next
                    x.next = y
            return k+1
        if head.next == None:
          return []
        xx = digui(head)
        if xx == n:
            return head.next
        return head
