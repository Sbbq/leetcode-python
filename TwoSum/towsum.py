# -*- coding: utf-8 -*-
#用hash表记录之前是否出现过target-nums[i]
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap={}
        for i in range(len(nums)):
            if target-nums[i] not in hashMap:
                hashMap[nums[i]]=i
            else:
                return hashMap[target-nums[i]],i
