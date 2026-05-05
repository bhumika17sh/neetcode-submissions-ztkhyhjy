class Solution:
    def tribonacci(self, n: int) -> int:
        dp={0:0,1:1,2:1}
        def ans(i):
            if i in dp:
                return dp[i]
            dp[i]=ans(i-1)+ans(i-2)+ans(i-3)
            return dp[i]
        return ans(n)
