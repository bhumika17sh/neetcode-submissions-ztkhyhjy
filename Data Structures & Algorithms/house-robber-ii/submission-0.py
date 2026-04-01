class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        #recursion
        # def solve(arr):
        #     def maxsum(i):
        #         if i<0:
        #             return 0
        #         if i==0:
        #             return arr[0]
        #         return max(arr[i]+maxsum(i-2),maxsum(i-1))
        #     return maxsum(len(arr)-1)
        # return max(solve(nums[:-1]), solve(nums[1:]))

        #bottom up 
        # def ans(nums):
        #     n=len(nums)
        #     if n==0:
        #         return 0
        #     if n==1:
        #         return nums[0]
        #     if n==2:
        #         return max(nums[0],nums[1])
        #     dp=[0]*n
        #     dp[0]=nums[0]
        #     dp[1]=max(nums[0],nums[1])
        #     for i in range(2,n):
        #         dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        #     return dp[n-1]
        # one=ans(nums[:-1])
        # two=ans(nums[1:])
        # return max(one,two)

        #bottom up with space optimisation
        def ans(nums):
            n=len(nums)
            if n==0:
                return 0
            if n==1:
                return nums[0]
            if n==2:
                return max(nums[0],nums[1])
            prev=nums[0]
            cur=max(nums[0],nums[1])
            for i in range(2,n):
                prev,cur=cur,max(cur,nums[i]+prev)
            return cur
        one=ans(nums[:-1])
        two=ans(nums[1:])
        return max(one,two)