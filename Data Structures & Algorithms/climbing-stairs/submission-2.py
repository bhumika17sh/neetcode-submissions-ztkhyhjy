class Solution:
    def climbStairs(self, n: int) -> int:

        #top down(memoization)
        # dp={}
        # if n in dp:
        #     return dp[n]
        # if n<=2:
        #     return n
        # dp[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
        # return dp[n] 

        #bottomup(tabulation)
        # if n<=2:
        #     return n
        # dp=[0]*(n+1)
        # dp[1], dp[2]=1, 2
        # for i in range(3,n+1):
        #     dp[n]=self.climbStairs(i-1)+self.climbStairs(i-2)
        # return dp[n]

        #optimised bottom up
        if n<=2:
            return n 
        prev=1
        cur=2
        for i in range(3,n+1):
            prev,cur = cur,prev+cur
        return cur
