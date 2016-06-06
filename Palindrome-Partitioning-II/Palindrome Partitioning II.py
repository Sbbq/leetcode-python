# -*- coding: utf-8 -*-
#一道很好的dp题目
#if s[i:j+1] is a palin mincount[i+r1+1]=min(mincount[i+r1+1],mincount[i-r1]+1)
#然后就是枚举i处所有的回文,更新mincount.
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        #为了处理好直接是回文的情况,mincount[i]为s[:i]的mincut,初值设为最大全切割的情况
        mincount=[x for x in range(-1,len(s))]
        for i in range(len(s)):
            r1,r2=0,0
            while(r1<=i and r1+i<len(s) and s[i-r1]==s[i+r1]):
                mincount[i+r1+1]=min(mincount[i+r1+1],mincount[i-r1]+1)
                r1+=1
            while(r2<=i and r2+i<len(s) and s[i-r2-1]==s[i+r2]):
                mincount[i+r2+1]=min(mincount[i+r2+1],mincount[i-r2-1]+1)
                r2+=1
        return mincount[-1]
