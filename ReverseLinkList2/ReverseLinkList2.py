#-*- coding:utf-8 –*-
#遍历整个链表的同时，将正在访问的节点then插入到链表头部，然后then=start.next
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        for i in range(m-1):
            pre=pre.next
        start=pre.next
        then=start.next
        for i in range(n-m):
            start.next=then.next
            then.next=pre.next
            pre.next=then
            then=start.next
        return dummy.next
