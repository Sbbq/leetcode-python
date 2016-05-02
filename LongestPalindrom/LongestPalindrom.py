# -*- coding: utf-8 -*-
#记的max[p]-1为原最长回文长度，自己理解下
#p[i]为i点的最长回文半径，mx为回文最右端的边界，id为此回文中心
#p[2*id-i]为i关于id的对称点，因为在回文内，所以p[i]=min(p[2*id-i],mx-i)
#剩下的在mx外的需要老老实实去匹配
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        t='@#'+'#'.join(s)+'# '
#没有@和空格的话会在i+pi处有边界问题
        p=[0]*len(t)
        id=1 
        mx=1
        for i in range(1,len(t)-1):
            p[i]=min(p[2*id-i],mx-i) if mx>i else 1
            while(t[i+p[i]]==t[i-p[i]]):
                p[i]+=1
            if i+p[i]>mx:
                mx=i+p[i]
                id=i
        inx=p.index(max(p))
        return s[(inx-max(p))/2:(inx-max(p))/2+max(p)-1]
