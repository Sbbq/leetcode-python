class Solution1(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def vaild(root,minnum,maxnum):
            if root==None :
                return True
            if root.val<=minnum or root.val>=maxnum:
                return False
            return vaild(root.left,minnum,root.val) and vaild(root.right,root.val,maxnum)
        return vaild(root,float('-inf'),float('inf'))
#利用中序遍历搜索树后为递增序列判断搜索树是否有效，以下用的堆栈版中序遍历
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        stack=[]
        prev=None
        #中序遍历的前一个节点
        while(stack or root):
            while(root):
                stack.append(root)
                root=root.left
            root=stack.pop()
            if prev and prev.val>=root.val:
                return False
            prev=root
            root=root.right
        return True
