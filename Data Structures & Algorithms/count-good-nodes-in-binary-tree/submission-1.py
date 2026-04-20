# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def dfs(node,maxx):
            nonlocal count
            if not node:
                return
            if node.val >=maxx:
                count+=1
                maxx=node.val
            dfs(node.right,maxx)
            dfs(node.left,maxx)

        dfs(root,root.val)
        return count
        
        
        # highestSoFar = root.val
        # res = 0

        # def findGoodNodes(node, highestSoFar):
        #     nonlocal res
        #     highestSoFar = max(highestSoFar, node.val)

        #     if node.val >= highestSoFar:
        #         res += 1
            

        #     if node.left:
        #         findGoodNodes(node.left, highestSoFar)
        #     if node.right:
        #         findGoodNodes(node.right, highestSoFar)
        
        # findGoodNodes(root, highestSoFar)
        # return res
