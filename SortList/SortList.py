#弄了半天没搞懂的地方就在那个prev.next=None
#将List分为两段
#然后就是递归还是不熟。。。。
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def MergeSort(head):
            if head==None or head.next==None:
                return head
            slow,fast,prev=head,head,None
            #这里用快慢两个节点，相当于归并的mid=(start+end)/2
            while(fast!=None and fast.next!=None):
                fast=fast.next.next
                prev=slow
                slow=slow.next
            prev.next=None
            #从mid处分裂两个链表
            l1=MergeSort(head)
            l2=MergeSort(slow)
            return Merge(l1,l2)
        def Merge(l1,l2):
            dummy=ListNode(-1)
            cur=dummy
            while(l1 and l2):
                if l1.val<=l2.val:
                    cur.next,l1=l1,l1.next
                else:
                    cur.next,l2=l2,l2.next
                cur=cur.next
            cur.next=l1 if l1 else l2
            return dummy.next
        return MergeSort(head)
