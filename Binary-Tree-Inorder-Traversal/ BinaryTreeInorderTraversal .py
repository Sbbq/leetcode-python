#-*- coding:utf-8 –*-
#中序遍历二叉树，迭代，设置一个堆栈
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        out=[]
        stack=[]
        cur=root
        while(stack or cur):
            #先移到最左子树
            while(cur):
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            out.append(cur.val)
            cur=cur.right
        return out
