class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        #bottom up
        if n==1:
            return nums[0]
        dp=[0]*n
        dp[0]=nums[0]
        dp[1]= max(nums[0],nums[1])
        for i in range(2,n):
            dp[i]=max(nums[i]+dp[i-2],dp[i-1])
        return dp[n-1]


        #bottom up with space optimisation
        #if n==1:
        #   return nums[0]
        # prev= nums[0]
        # cur=max(nums[0],nums[1])
        # for i in range(2,n):
        #     prev,cur=cur,max(nums[i]+prev,cur)

        # return cur
        #top down
        # if n==1:
        #     return nums[0]
        # if n==2:
        #     return max(nums[0],nums[1])
        # dp={0:nums[0],1:max(nums[0],nums[1])}
        # def helper(i):
        #     if i in dp:
        #         return dp[i]
        #     else:
        #         dp[i]=max(nums[i]+helper(i-2),helper(i-1))
        #     return dp[i]
        # return helper(n-1)