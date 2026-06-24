class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        cou=prerequisites
        for u,v in cou:
            graph[u].append(v)
        unvisit=0
        visiting=1
        visited=2
        ans=[unvisit]*numCourses
        

        def dfs(node):
            state=ans[node]
            if state==visited:
                return True
            elif state==visiting:
                return False
            ans[node]=visiting
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            ans[node]=visited
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
