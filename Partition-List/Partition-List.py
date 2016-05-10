#do more practise
#first do next and then n1=n1.next
#concentrate on head ok  head.next is the begin
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        p1=n1=ListNode(0)
        p2=n2=ListNode(0)
        while(head):
            if head.val<x:
                n1.next=head
                n1=n1.next
            else:
                n2.next=head
                n2=n2.next
            head=head.next
        n2.next=None
        n1.next=p2.next
        return p1.next
