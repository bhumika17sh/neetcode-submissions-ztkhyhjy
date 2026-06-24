class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins=-1
        empty,fresh,rotten=0,1,2
        m,n=len(grid),len(grid[0])
        q=deque()
        fresh_num=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==rotten:
                    q.append((i,j))
                elif grid[i][j]==fresh:
                    fresh_num+=1
                
                    
        if fresh_num==0:
            return 0
        while q:
            q_size=len(q)
            mins+=1
            for _ in range(q_size):
                i,j=q.popleft()
                for r,c in [(i,j+1),(i+1,j),(i-1,j),(i,j-1)]:
                    if 0<=r<m and 0<=c<n and grid[r][c]==fresh:
                        grid[r][c]=rotten
                        fresh_num-=1
                        q.append((r,c))
        if fresh_num==0:
            return mins
        else:
            return -1