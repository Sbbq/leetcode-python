# -*- coding: utf-8 -*-
#服
#利用一种递增波峰图计算矩形面积
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack=[-1]
        ans=0
        heights.append(0)
        for i in range(len(heights)):
            while (heights[i]<heights[stack[-1]]):
                h=heights[stack.pop()]
                w=i-stack[-1]-1
                ans=max(ans,h*w)
            stack.append(i)
        return ans
