#一直在想怎么遍历，其实最好的遍历就是利用他的next
#记录最左边的节点为cur，写他的下一层节点的next
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root==None:
            return
        cur=TreeLinkNode(-1)
        while(root.left!=None):
            cur=root
            while(cur!=None):
                cur.left.next=cur.right
                if cur.next!=None:
                    cur.right.next=cur.next.left
                cur=cur.next
            root=root.left
