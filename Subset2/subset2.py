#to use iterate add a new parameter previsize to sub the old subset
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        nums.sort()
        for i in range(len(nums)):
            size=len(res)
            if i>0 and nums[i]==nums[i-1]:
                res+=[x+[nums[i]] for x in res[previsize:] ]
            else:
                res+=[x+[nums[i]] for x in res ]
            previsize=size
        return res
