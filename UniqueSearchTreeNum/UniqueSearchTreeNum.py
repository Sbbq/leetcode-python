#-*- coding:utf-8 –*-
#起码看懂思路了,假设G[i]=当n为i时二叉树的数量，f(i,n)表示以i为根节点的二叉树数量
#G[n]=f(1,n)+f(2,n)+...+f(n,n),f(i,n)又分为左右子树，左子树的个数为G[i-1],右子树个数为G[n-i],f(i,n)=G[i-1]*G[n-i]
#G[n]=G[0]*G[n-1]+G[1]*G[n-2]+...+G[n-1]*G[0]
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        G=[0]*(n+1)
        G[0]=1
        for i in range(1,n+1):
            for j in range(i):
                G[i]+=G[j]*G[i-j-1]
        return G[-1]
