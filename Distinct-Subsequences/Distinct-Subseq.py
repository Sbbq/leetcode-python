#t为行,s为列,t为空dp[0][j]=1,s为空dp[i][0]=0
#s[j]==t[i]时,考虑用不用s[j],dp[i][j]=dp[i][j-1]+dp[i-1][j-1],不等就为dp[i][j]=dp[i][j-1]
#dp类题目，先想好空串的情况，然后找规律
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m,n=len(s),len(t)
        dp=[[0 for j in range(n+1)] for i in range(m+1)]
        dp[0][0]=1
        for i in range(m):
            dp[i][0]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]
