class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i=m
        j=0
        while j<n:
            nums1[i]=nums2[j]
            i+=1
            j+=1
        nums1.sort()
        # takes time
        # nums1.sort()
        # i=j=0
        # while i<len(nums1) and j<len(nums2):
        #     if nums1[i]==0:
        #         nums1[i]=nums2[j]
        #         i+=1
        #         j+=1
        # return nums1