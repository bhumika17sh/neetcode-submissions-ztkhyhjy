class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # return nums
        # merge sort
        def merge_sort(arr):
            if len(arr)<=1:
                return arr
            mid=len(arr)//2
            left=merge_sort(arr[:mid])
            right=merge_sort(arr[mid:])
            return merge(left,right)
        def merge(left,right):
            i=j=0
            res=[]
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            return res+left[i:]+right[j:]
        return merge_sort(nums)