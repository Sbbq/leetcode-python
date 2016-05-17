#失误的地方：需要设置一个res
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        mx=float('inf')
        res=0
        for i in range(len(nums)-2):
            if i==0 or nums[i]!=nums[i-1]:
                left,right=i+1,len(nums)-1
                while(left<right):
                    if mx>abs(nums[i]+nums[left]+nums[right]-target):
                        res=nums[i]+nums[left]+nums[right]
                        mx=abs(nums[i]+nums[left]+nums[right]-target)
                    if nums[i]+nums[left]+nums[right]-target>0:
                        right-=1
                    elif nums[i]+nums[left]+nums[right]-target<0:
                        left+=1
                    else:
                        return target
        return res
