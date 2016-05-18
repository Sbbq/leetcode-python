#这个才是编程，造轮子太烦了
#最小堆来合并
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy=ListNode(-1)
        start=dummy
        h=[(n.val,n) for n in lists if n ]
        #建立一个列表，包含每个链表的头和表头的值
        heapq.heapify(h)
        #把h建立成一个最小堆
        while(h):
        #获取最小堆的最小值和他的链表头
            val,n=h[0]
            if n.next==None:
            #当某个链表取完时，不插入直接返回
                heapq.heappop(h)
            else:
            #先pop再push，pop的值之前记录过了，插入n.next.val和n.next
                heapq.heapreplace(h,(n.next.val,n.next))
            start.next=n
            start=start.next
        return dummy.next
