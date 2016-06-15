#很好的dfs程序
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res=[]
        path=[]
        def dfs(s,res,path):
        #出循环的条件s为空
            if not s:
                res.append(path)
                return 
            for i in range(1,len(s)+1):
                if s[:i]==s[i-1::-1]:
                #注意s是变化的，只要s[:i]是回文，就加入到path
                    dfs(s[i:],res,path+[s[:i]])
        dfs(s,res,path)
        return res
