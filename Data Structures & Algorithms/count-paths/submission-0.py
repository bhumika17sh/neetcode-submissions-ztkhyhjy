class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #recursive
        # def path(i,j):
        #     if i==j==0:
        #         return 1
        #     elif i<0 or j<0 or i ==m or j==n:
        #         return 0
        #     else:
        #         return path(i-1,j)+path(i,j-1)
        # return path(m-1,n-1)

        #memoization
        memo={(0,0):1}
        def path(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            elif i<0 or j<0 or i ==m or j==n:
                return 0
            else:
                val=path(i-1,j)+path(i,j-1)
                memo[(i,j)]=val
                return val
        return path(m-1,n-1)

        #bottomup
        # dp=[]
        # for _ in range(m):
        #     dp.append([0]*n)
        # dp[0][0]=1
        # for i in range(m):
        #     for j in range(n):
        #         if i==j==0:
        #             continue
        #         val=0
        #         if i>0:
        #             val+=dp[i-1][j]
        #         if j>0:
        #             val+=dp[i][j-1]
        #         dp[i][j]=val
        # return dp[m-1][n-1]
