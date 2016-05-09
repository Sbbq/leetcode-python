# -*- coding: utf-8 -*-
#i在记录的是没重复超过两次的数的坐标
class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
            #和两次存进去前相比，相同就说明重复3次，不同就存进去，i+=1
                nums[i] = n
                i += 1
        return i


if __name__ == "__main__":
    print Solution().removeDuplicates([4,4,4,5,5,6])
pass
