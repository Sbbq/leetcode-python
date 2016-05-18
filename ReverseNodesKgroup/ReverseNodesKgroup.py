#庆祝自己第一次hard一次通过
#编程就是先想好怎么编，不是边编边想
#将链表倒序这个方法很好用，就是选个一个go节点，不停的插入表头，当go到尾巴，即倒序完成
#编写一个varify用于验证是否够节点倒序
#倒序之后，更新start节点为end节点，循环倒序直到varify不通过
class ListNode(object):
    def __init__(self, x):
        self.val = x
       self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k==1:
            return head
        dummy=start=ListNode(-1)
        dummy.next=head
        def varify(head,k):
            end=head
            while(k>0 and end!=None):
                end=end.next
                k-=1
            if end!=None:
                return True
            else:
                return False
        def transform(start,k):
            while(varify(start,k)):
                end=start.next
                go=end.next
                for i in range(k-1):
                    end.next=go.next
                    go.next=start.next
                    start.next=go
                    go=end.next
                start=end
        transform(start,k)
        return dummy.next
