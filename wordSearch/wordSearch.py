# -*- coding: utf-8 -*-
#dfs最笨也最实用要掌握
#首先记得解决重复问题，取‘#’，其次是那3个or的返回问题，每次都会返回False or True
#dfs只是对每次的输入做判断
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i,j,board,word):
            if len(word)==0:
                return True
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!=word[0]:
                return False
            temp=board[i][j]
            board[i][j]='#'
            res=dfs(i+1,j,board,word[1:]) or dfs(i-1,j,board,word[1:]) or dfs(i,j+1,board,word[1:]) or dfs(i,j-1,board,word[1:])
            board[i][j]=temp
            return res
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,board,word):
                    return True
        return False
