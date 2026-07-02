class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # recursive
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # def path(i,j):
        #     if i==j==0:
        #         return 1
        #     if i>=0 and j>=0 and obstacleGrid[i][j]==1:
        #           return 0
        #     elif i<0 or j<0 or i ==m or j==n:
        #         return 0
        #     else:
        #         return path(i-1,j)+path(i,j-1)
        # return path(m-1,n-1)

        # memo={}
        # def path(i,j):
        #     if i>=0 and j>=0 and obstacleGrid[i][j]==1:
        #         return 0
        #     if i<0 or j<0 or i==m or j==n:
        #         return 0
        #     if (i,j)==(0,0):
        #         return 1
        #     if (i,j) in memo:
        #         return memo[(i,j)]
            
        #     val=path(i-1,j)+path(i,j-1)
        #     memo[(i,j)]=val
        #     return val
        # return path(m-1,n-1)


        dp=[]
        for _ in range(m):
            dp.append([0]*n)

        if obstacleGrid[0][0]==1:
            return 0
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if i==j==0:
                    continue
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    val=0
                    if i>0:
                        val+=dp[i-1][j]
                    if j>0:
                        val+=dp[i][j-1]
                    dp[i][j]=val
        return dp[m-1][n-1]