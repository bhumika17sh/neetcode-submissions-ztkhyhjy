class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # current=nums[0]
        # maxx=nums[0]
        # for i in range(1,len(nums)):
        #     current=max(nums[i],current+nums[i])
        #     maxx=max(maxx,current)
        # return maxx

        curr=0
        maxx=float('-inf')
        for num in nums:
            curr+=num
            maxx=max(maxx,curr)
            curr=max(curr,0)
        return maxx