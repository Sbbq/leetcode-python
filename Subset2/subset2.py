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
#dfs
class Solution2(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        path=[]
        nums.sort()
        #should sort first
        def dfs(nums,path,res,i):
            res+=path,
            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                #j>i not j>0
                    continue
                else:
                    dfs(nums,path+[nums[j]],res,j+1)
        dfs(nums,path,res,0)
        return res
