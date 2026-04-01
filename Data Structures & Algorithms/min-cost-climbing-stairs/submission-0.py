class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #top down approach
        # n=len(cost)
        # dp={0:0,1:0}
        # def mincost(i):
        #     if i in dp:
        #         return dp[i]
        #     dp[i]=min(cost[i-2]+mincost(i-2),cost[i-1]+mincost(i-1))
        #     return dp[i]
        # return mincost(n)

        #bottom up approach
        n=len(cost)
        dp=[0]*(n+1)
        for i in range(2,n+1):
            dp[i]=min(cost[i-2]+dp[i-2],cost[i-1]+dp[i-1])
        return dp[n]