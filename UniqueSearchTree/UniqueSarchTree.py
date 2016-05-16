#-*- coding:utf-8 –*-
#递归哎，不停的构建子树，并建立新的res包含所有子树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n==0:
            return []
        def generateTreesRecu(start, end):
            res=[]
            if start>end:
                res.append(None)
            for i in xrange(start,end+1):
                l=generateTreesRecu(start,i-1)
                r=generateTreesRecu(i+1,end)
                for x in l:
                    for y in r:
                        temp=TreeNode(i)
                        temp.left,temp.right=x,y
                        res.append(temp)
            return res
        return generateTreesRecu(1, n)
