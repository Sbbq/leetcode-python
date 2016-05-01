# -*- coding: utf-8 -*-
#写之前最好注意画个链表图，注意空链表没有next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res=ListNode(-1)
        head=res
        preVal=0
        while(l1 or l2 or preVal):
            preVal+=l1.val if l1!=None else 0
            preVal+=l2.val if l2!=None else 0
            res.next=ListNode(preVal%10)
            preVal=preVal/10
            res=res.next
            l1=l1.next if l1!=None else None
            l2=l2.next if l2!=None else None
        return head.next
