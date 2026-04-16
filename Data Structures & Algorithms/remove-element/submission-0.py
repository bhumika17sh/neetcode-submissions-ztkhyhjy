class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Extra space
        # ans=[]
        # for i in nums:
        #     if i!=val:
        #         ans.append(i)
        # nums[:len(ans)]=ans
        # return len(ans)

        # two pointer
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k