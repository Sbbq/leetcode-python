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
#任意二叉树
#每层设置一个空节点nextleft，记录开头,cur遍历
#记录上一层root
class Solution2(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if root==None:
            return
        while(root!=None):
            nextleft=TreeLinkNode(-1)
            cur=nextleft
            while(root!=None):
                if root.left!=None:
                    cur.next=root.left
                    cur=cur.next
                if root.right!=None:
                    cur.next=root.right
                    cur=cur.next
                root=root.next
            root=nextleft.next
            nextleft=None
