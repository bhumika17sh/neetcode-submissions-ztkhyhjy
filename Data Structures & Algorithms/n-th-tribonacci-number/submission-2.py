class Solution:
    def tribonacci(self, n: int) -> int:
        # dp={0:0,1:1,2:1}
        # def ans(i):
        #     if i in dp:
        #         return dp[i]
        #     dp[i]=ans(i-1)+ans(i-2)+ans(i-3)
        #     return dp[i]
        # return ans(n)
        
        #bottom up
        # if n == 0:
        #     return 0
        # if n <= 2:
        #     return 1
        
        # dp = [0] * (n + 1)
        # dp[0], dp[1], dp[2] = 0, 1, 1
        
        # for i in range(3, n + 1):
        #     dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        
        # return dp[n]

        # space optimised
        if n == 0:
            return 0
        if n <= 2:
            return 1 
        
        a,b,c = 0,1,1

        for _ in range(3,n+1):
            a,b,c = b,c,(a+b+c)
        
        return c