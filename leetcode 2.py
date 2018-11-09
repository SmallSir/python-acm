'''
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        k = 0
        sum = ListNode(0)
        head = sum
        while l1 or l2:
            if l1:
                k += l1.val
                l1 = l1.next
            if l2:
                k += l2.val
                l2 = l2.next
            sum.next = ListNode(k%10)
            sum = sum.next
            k = k//10
        if k !=0 :
            sum.next = ListNode(1)
            sum = sum.next
        return head.next
'''


def get_fib(index):
    n,a,b = 0,0,1
    while n < index:
        yield b
        a,b = b,a+b
        n+=1
if __name__ == '__main__':
    print(get_fib(10))