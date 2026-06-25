class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit=set()
        m,n=len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]!=1:
                return 1
            if (i,j) in visit:
                return 0
            visit.add((i,j))
            perimeter=dfs(i,j+1)+dfs(i+1,j)+dfs(i,j-1)+dfs(i-1,j)
            return perimeter
            

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    return dfs(i,j)

        return 0