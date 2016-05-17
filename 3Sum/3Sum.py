#注意怎么处理重复问题。
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        for i in range(len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                left,right,sums=i+1,len(nums)-1,-nums[i]
                while(left<right):
                    if nums[left]+nums[right]==sums:
                        res.append([nums[left],nums[right],nums[i]])
                        while(nums[right]==nums[right-1] and left<right-1):
                            right-=1
                        while(nums[left]==nums[left+1] and left+1<right):
                            left+=1
                        #下面两行漏掉了，注意上面只有相等才移位，不等就不移动了
                        left+=1
                        right-=1
                    elif nums[left]+nums[right]>sums:
                        right-=1
                        while(nums[right]==nums[right+1]and left<right):
                            right-=1
                    else:
                        left+=1
                        while(nums[left-1]==nums[left] and left<right):
                            left+=1
        return res
