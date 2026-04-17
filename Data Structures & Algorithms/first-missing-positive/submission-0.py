class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        while i<n:
            correct=nums[i]-1
            if 1<=nums[i]<=n and nums[i]!=nums[correct]:
                nums[i],nums[correct]=nums[correct],nums[i]
            else:
                i+=1
        for i in range(n):
            if nums[i]!=i+1:
                return i+1        
        return n+1
        # nums.sort()
        # missing=1
        # for num in nums:
        #     if num==missing:
        #         missing+=1
        #     elif num>missing:
        #         return missing
        # return missing

        # if nums[-1]==0:
        #     return 1
        # else:
        #     for i in range(len(nums)):
        #         if nums[i]-nums[i-1] <=1:
        #             continue
        #         return nums[i]-1
                
        