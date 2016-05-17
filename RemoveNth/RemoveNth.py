class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#这里的头结点是链表的第一个元素，不是表头，设置一个表头可以很好解决NoneType has no next的问题
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy=ListNode(-1)
        dummy.next=head
        start,low=dummy,dummy
        while(n>0):
            start=start.next
            n-=1
        while(start.next!=None):
            start=start.next
            low=low.next
        obj=low.next
        low.next=obj.next
        obj.next=None
        return dummy.next
