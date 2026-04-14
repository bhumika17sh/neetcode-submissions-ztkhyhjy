class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        visited=[False]*len(nums)
        def backtrack(path):
            if len(path)==len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                path.append(nums[i])
                visited[i]=True
                backtrack(path)

                path.pop()
                visited[i]=False
        backtrack([])
        return res 