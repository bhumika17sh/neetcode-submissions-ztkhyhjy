class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=sorted(nums1+nums2)
        n=len(nums)
        if n % 2 == 1:

            return nums[n // 2]

        else:

            return (nums[n//2 - 1] + nums[n//2]) / 2
        
        # nums=[]
        # k=0
        # i,j=0,0
        # while i<len(nums) and j<len(nums):
        #     if nums[i]<nums[j]:
        #         nums.append(nums1[i])
        #         i+=1
        #     else:
        #         nums.append(nums2[j])
        #         j+=1
        # while i<len(nums1):
        #     nums.append(nums1[i])
        #     i+=1
        # while j<len(nums2):
        #     nums.append(nums2[j])
        #     j+=1
        # n=len(nums)
        # if n%2:
        #     return nums[n//2]
        # else:
        #     return (nums[n//2-1]+nums[n//2])/2