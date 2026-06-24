class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_que=deque()
        pseen=set()

        a_que=deque()
        aseen=set()

        m,n=len(heights),len(heights[0])

        for j in range(n):
            p_que.append((0,j))
            pseen.add((0,j))
        for i in range(1,m):
            p_que.append((i,0))
            pseen.add((i,0))
        for i in range(m):
            a_que.append((i,n-1))
            aseen.add((i,n-1))
        for j in range(n-1):
            a_que.append((m-1,j))
            aseen.add((m-1,j))
        def get(que,seen):
            coords=set()
            while que:
                i,j=que.popleft()
                for ioff,joff in [(0,1),(1,0),(-1,0),(0,-1)]:
                    r,c=i+ioff,j+joff
                    if 0 <= r < m and 0 <= c < n and heights[r][c] >=heights[i][j] and (r,c) not in seen:
                    
                        seen.add((r,c))
                        que.append((r,c))
        get(p_que,pseen)
        get(a_que,aseen)
        return list(pseen.intersection(aseen))