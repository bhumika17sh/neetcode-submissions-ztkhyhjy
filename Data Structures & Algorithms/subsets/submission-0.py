class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # iterative brute force
        # ans=[[]]
        # for num in nums:
        #     new_subsets=[]
        #     for subset in ans:
        #         new_subsets.append(subset+[num])
        #     ans.extend(new_subsets)
        # return ans
            
        #backtracking
        res=[]
        def backtrack(index,path):
            if index==len(nums):
                res.append(path.copy())
                return
            path.append(nums[index])
            backtrack(index+1,path)
            path.pop()
            backtrack(index+1,path)
        backtrack(0,[])
        return res