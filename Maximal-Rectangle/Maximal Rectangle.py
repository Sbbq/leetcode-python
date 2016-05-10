#the key is to compute height and then combine Largest Rectangle
class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(len(matrix[0])):
                height[i]=height[i]+1 if row[i]=='1' else 0
            stack=[-1]
            for j in range(len(height)):
                while(height[j]<height[stack[-1]]):
                    h=height[stack.pop()]
                    w=j-stack[-1]-1
                    ans=max(ans,h*w)
                stack.append(j)
        return ans
