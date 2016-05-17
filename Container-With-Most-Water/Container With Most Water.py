#用双指针，体积由短板决定，每次移动小的指针到大于指针高度，算一次体积
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        mmx=0
        while(left<right):
            v=min(height[left],height[right])*(right-left)
            mmx=max(mmx,v)
            if height[left]<=height[right]:
                i=left+1
                while(height[i]<height[left]):
                    i+=1
                left=i
            else:
                i=right-1
                while(height[i]<height[right]):
                    i-=1
                right=i
        return mmx
