#很好的递归+dp练习题
#用dp记录已经肯定的以i,j开头的最大长度，递归的计算所有i,j
#当dp等于0，表示未计算，依靠周围的dp计算，直到周围都肯定了
#当dp有值就直接返回
#递归的题目，就把递归当成一个函数看，不要循环看
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if matrix==[]:
            return 0
        dp=[[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        m,n=len(matrix),len(matrix[0])
        def dfs(x,y):
            if not dp[x][y]:
                dp[x][y]=1+max(dfs(x-1,y) if x and matrix[x][y]<matrix[x-1][y] else 0,
                               dfs(x+1,y) if x<m-1 and matrix[x][y]<matrix[x+1][y] else 0,
                               dfs(x,y+1) if y<n-1 and matrix[x][y]<matrix[x][y+1] else 0,
                               dfs(x,y-1) if y and matrix[x][y]<matrix[x][y-1] else 0)
            return dp[x][y]
        return max(dfs(x,y) for x in range(m) for y in range(n))
