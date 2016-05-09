# -*- coding: utf-8 -*-
#位图，共有子集1<<N个，每一位代表是否选择nums的元素
class Solution(object):
    def subsets(self, nums):
            N  = len(nums)
            subset_num = 1<<N
            result = [[] for _ in range(subset_num)]
            nums.sort()
            for i in range(N):
            #所有子集中取第i位的有
                for j in range(subset_num):
                #对于第j种子集来说，是否取第i位
                    if (j >> i) & 1: result[j].append(nums[i])
            return result
#迭代，真心666
#第一次[],第二次[]+[1],第三次[]+[1]+[3]+[1,3]...
#每次都由上次的res+[num]
class Solution1(object):
    def subsets(self, nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res


if __name__ == "__main__":
    print Solution().subsets([4,3,1])
