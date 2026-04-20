# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if not root:
            return []
        q=deque([root])
        while q:
            size=len(q)
            for i in range(size):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i==size-1:
                    ans.append(node.val)
        return ans
        #DFS
        # ans=[]
        # def dfs(node,level):
        #     if not node:
        #         return
        #     if level==len(ans):
        #         ans.append(node.val)
        #     dfs(node.right,level+1)
        #     dfs(node.left,level+1)
        # dfs(root,0)
        # return ans