# -*- coding: utf-8 -*-
#排序可以有效应对这种回文啦的题目，排序后，他们都变为一种了
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dit={}
        for i in sorted(strs):
            key=tuple(sorted(i))
            dit[key]=dit.get(key,[])+[i]
#用好检索，用字典
        return dit.values()
